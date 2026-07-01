from google.genai import types
import mysql.connector


def query_mysql_database(sql_query: str):
    """
    Executes a SQL query against the MySQL database and returns the results.
    Args:
        sql_query: A valid MySQL SELECT statement.
    """
    print("this is the sql query : ", sql_query)
    try:
        # Connect to your MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mog_demo" # e.g., 'school' or 'bbms'
        )
        cursor = db.cursor(dictionary=True)
        
        cursor.execute(sql_query)
        results = cursor.fetchall()
        
        cursor.close()
        db.close()
        
        return str(results) if results else "No records found."
    except Exception as e:
        return f"Error executing query: {str(e)}"
    
def sql_agent(client): 
    # Define the tools for the model
    tools = [query_mysql_database]
    # System Instruction is CRITICAL here
    system_prompt = """
    You are a Database Analyst for the AURA-X system.
    You have access to a MySQL database. 

    Instructions:
    1. Use the 'query_mysql_database' tool to fetch data.
    2. If the user asks a question, translate it into a valid MySQL SELECT statement.
    3. Only answer based on the data returned by the tool.
    4. If you don't know the table names, ask the user or try to 'SHOW TABLES'.
    """

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
    )

    chat = client.chats.create(
        model="gemma-4-31b-it", # Recommended for reliable Tool Use
        config=config
    )

    return chat

def call_llm(client, messages):
    # 1. Extract the latest user message (the last item in your list)
    user_message = messages[-1]["content"]
    
    # 2. Extract and format the history (everything except the last message)
    # Note: Google SDK expects role to be 'user' or 'model'
    history = []
    for m in messages[:-1]:
        # Map 'assistant' or 'system' (from your RAG/Memory) to 'model'
        role = "model" if m["role"] in ["assistant", "system"] else "user"
        history.append(types.Content(
            role=role,
            parts=[types.Part.from_text(text=m["content"])]
        ))

    system_instruction = """
        You are an advanced AI Document Analyzer.

        Your role:
        - Analyze provided documents and answer user questions based ONLY on the given context.
        - Extract key insights, summaries, and relevant facts from documents.
        - If multiple documents are provided, compare and synthesize them.

        Rules:
        1. Always prioritize document context over general knowledge.
        2. If the answer is found in documents, cite or reference it clearly.
        3. If the answer is NOT in the provided documents, say:
        "The answer is not found in the provided documents."
        4. Be precise, structured, and concise.
        5. When appropriate, format answers using:
        - bullet points
        - short explanations
        - summaries

        Capabilities:
        - Summarization
        - Question answering
        - Key point extraction
        - Risk detection (e.g. phishing, suspicious content)
        - Explanation of technical or non-technical content

        Tone:
        - Clear
        - Professional
        - Helpful (like an analyst, not a chatbot)

        Never:
        - Hallucinate missing information
        - Make assumptions outside the document context

        and You are also a Database Analyst.
        You have access to a MySQL database. 

        Instructions:
        1. Use the 'query_mysql_database' tool to fetch data.
        2. If the user asks a question, translate it into a valid MySQL SELECT statement.
        3. Only answer based on the data returned by the tool.
        4. If you don't know the table names, ask the user or try to 'SHOW TABLES'.
        """

    # 3. Initialize chat with history
    chat = client.chats.create(
        model="gemma-4-31b-it", # Note: Ensure model name is correct for 2026
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0,  # Recommended for Document Analyzers
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
        ),
        history=history
    )

    # 4. Send ONLY the single string of the new message
    response = chat.send_message(user_message)

    return response.text

def router_agent(client, user_query):
    router_prompt = f"""
    Analyze the user request and categorize it into ONE of these two categories:
    1. 'DATABASE': If the user asks about structured data, student records, counts, or anything requiring a SQL query.
    2. 'DOCUMENT': If the user asks to analyze, summarize, or extract info from uploaded files/text context.

    User Request: "{user_query}"
    Output only the word 'DATABASE' or 'DOCUMENT'.
    """
    
    # Use a simple generate_content call for the router
    decision = client.models.generate_content(
        model="gemma-4-31b-it",
        contents=router_prompt
    ).text.strip()
    
    return decision

def general_agent(client):
    system_prompt = """
    You are an AI assistat which can answer general questions.

    Instructions:
    chat with the user in a friendly way mainly use burmese language.
    """

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
    )

    chat = client.chats.create(
        model="gemma-4-31b-it", # Recommended for reliable Tool Use
        config=config
    )

    return chat

