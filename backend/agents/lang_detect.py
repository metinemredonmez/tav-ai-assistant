
def detect_language(state):
    question = state.get("question", "")
    lang = "tr" if "kaçta" in question or "ne zaman" in question else "en"
    return {"language": lang, "question": question}
