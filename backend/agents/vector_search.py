
def search_flight(state):
    question = state["question"]
    if "TK123" in question:
        return {"flight_info": "TK123 ucagi saat 14:45'te B16 kapisindan kalkacaktir."}
    elif "TK456" in question:
        return {"flight_info": "TK456 ucagi 16:30'da A4 kapisindan kalkacaktir."}
    return {"flight_info": "Ucus bulunamadi."}
