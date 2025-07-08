
from fastapi import FastAPI, Request
from langgraph.graph import StateGraph
from backend.mcp_wrapper import MCPWrapper
from agents.lang_detect import detect_language
from agents.vector_search import search_flight
from agents.answer_synth import generate_answer
import uvicorn

# MCP-enabled LangGraph workflow
graph = StateGraph()
graph.add_node("lang_detect", MCPWrapper(detect_language, "LangDetect").run)
graph.add_node("vector_search", MCPWrapper(search_flight, "VectorSearch").run)
graph.add_node("answer_synth", MCPWrapper(generate_answer, "AnswerSynth").run)

graph.set_entry_point("lang_detect")
graph.add_edge("lang_detect", "vector_search")
graph.add_edge("vector_search", "answer_synth")
graph.set_finish_point("answer_synth")
workflow = graph.compile()

# FastAPI Web server
app = FastAPI()

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    result = workflow.invoke({"question": question})
    return {"response": result.get("answer", "Cevap bulunamadi.")}

@app.get("/")
async def root():
    return {"message": "TAV AI Assistant with LangGraph + MCP"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
