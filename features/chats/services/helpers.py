def format_context(context):
    return "\n".join([
        f"{c['role'].upper()}: {c['content']}"
        for c in context if c.get("content")
    ])