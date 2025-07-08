
class MCPWrapper:
    def __init__(self, agent_fn, name):
        self.agent_fn = agent_fn
        self.name = name

    def run(self, state):
        try:
            print(f"[{self.name}] >> Input: {state}")
            result = self.agent_fn(state)
            print(f"[{self.name}] ✅ Output: {result}")
            return result
        except Exception as e:
            print(f"[{self.name}] ❌ Error: {e}")
            return {"error": str(e), "agent": self.name}
