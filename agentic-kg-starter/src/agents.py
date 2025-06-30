import requests
from dataclasses import dataclass, field

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

def llm(prompt: str, model="mistral"):
    res = requests.post(OLLAMA_ENDPOINT,
                        json={"model": model, "prompt": prompt,
                              "stream": False})
    json_response = res.json()
    if "response" in json_response:
        return json_response["response"]
    else:
        print(f"Error: 'response' key not found in Ollama response. Full response: {json_response}")
        # Depending on desired behavior, you might raise an exception, return an empty string, or handle differently.
        # For now, returning an empty string to allow the program to continue, but the error is logged.
        return ""

@dataclass
class Agent:
    name: str
    role: str
    system_prompt: str
    traits: dict = field(default_factory=dict)
    memory: list = field(default_factory=list)

    def build_prompt(self, user_in: str, retrieved: str = "") -> str:
        trait_line = f"You are a {self.role} with traits {self.traits}."
        context    = f"\nRelevant memory:\n{retrieved}" if retrieved else ""
        return f"{trait_line}{context}\n\nUser: {user_in}\n\nAgent:"

    def __call__(self, user_in: str, retrieved: str = "") -> str:
        prompt  = self.build_prompt(user_in, retrieved)
        output  = llm(prompt)
        self.memory.append({"input": user_in, "output": output})
        return output
