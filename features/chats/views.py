from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from google import genai

from .models import ChatMessage, Document
from .services.chat_memory import save_to_chroma, retrieve_memory
from .services.rag import store_document, retrieve_docs
from .services.summarizer import summarize
from .services.llm import call_llm, router_agent, sql_agent
from .services.helpers import format_context

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def chat(request):
    user = request.user
    message = request.data.get("message")
    client = genai.Client()
    file = request.FILES.get("file")  # 👈 optional
    print("this is the file ", file)

    # --- In your Django View ---
    request_type = router_agent(client, message)

    print("this is the request type : ", request_type)

    if request_type == "DATABASE" and file is None:

        # 🔹 Save user message
        if message:
            ChatMessage.objects.create(
                user_id=user.id,
                role="user",
                content=message
            )
            save_to_chroma(str(user.id), "user", message)

        # 🔹 Get recent chat
        recent = ChatMessage.objects.filter(user_id=user.id)\
            .order_by('-created_at')[:5]

        recent = [{"role": m.role, "content": m.content} for m in reversed(recent)]

        # 🔹 Retrieve memory (vector DB)
        memory = retrieve_memory(str(user.id), message)

        # 🔹 Build context for SQL agent
        context = memory + recent
        context.append({"role": "user", "content": message})

        context = format_context(context)
        # 🔹 Call SQL agent with context instead of plain message
        response = sql_agent(client).send_message(context)

        # 🔹 Save response
        ChatMessage.objects.create(
            user_id=user.id,
            role="assistant",
            content=response.text
        )
        save_to_chroma(str(user.id), "assistant", response.text)

        return Response({
            "response": response.text,
            "source": "database_with_memory"
        })

    if not message and not file:
        return Response({"error": "Message or file required"}, status=400)

    # ✅ 1. Handle file if exists
    if file:
        doc = Document.objects.create(file=file)
        store_document(doc.file.path)

    # ✅ 2. Save user message
    ChatMessage.objects.create(
        user_id=user.id,
        role="user",
        content=message
    )
    save_to_chroma(str(user.id), "user", message)

    # ✅ 3. Recent messages
    recent = ChatMessage.objects.filter(user_id=user.id)\
        .order_by('-created_at')[:5]

    recent = [{"role": m.role, "content": m.content} for m in reversed(recent)]

    # ✅ 4. Memory retrieval
    memory = retrieve_memory(str(user.id), message)

    # ✅ 5. Document retrieval (NOW includes uploaded file)
    docs = retrieve_docs(message)

    doc_context = [
        {"role": "system", "content": f"Document: {d}"}
        for d in docs
    ]

    # ✅ 6. Combine context
    context = doc_context + recent + memory
    
    context.append({"role": "user", "content": message})
    print("this is context and llm is about to be called!!", context)
    # ✅ 7. LLM
    
    response = call_llm(client, context)

    # ✅ 8. Save AI response
    ChatMessage.objects.create(
        user_id=user.id,
        role="assistant",
        content=response
    )
    save_to_chroma(str(user.id), "assistant", response)

    # ✅ 9. Summarization
    if ChatMessage.objects.filter(user_id=user.id).count() > 20:
        old_messages = ChatMessage.objects.filter(user_id=user.id).order_by('id')[:20]
        old_ids = list(old_messages.values_list('id', flat=True))

        summary = summarize(client, old_messages)

        ChatMessage.objects.create(
            user_id=user.id,
            role="system",
            content=summary
        )

        ChatMessage.objects.filter(id__in=old_ids).delete()

    return Response({
        "response": response,
        "docs_used": docs,
        "file_uploaded": bool(file)
    })