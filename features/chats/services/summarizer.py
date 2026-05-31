from .llm import call_llm

def summarize(client,messages):
    text = "\n".join([f"{m.role}: {m.content}" for m in messages])

    prompt = f"Summarize this conversation briefly:\n{text}"

    return call_llm(client,[{"role": "user", "content": prompt}])