import fire, networkx as nx
from src.agents import Agent
from src.graph_builder import build_basic_journal_graph

def journal(entry: str):
    analyzer  = Agent("Analyzer","tone-extractor",
                      "Extract emotions + themes.", {"curiosity":8})
    reflector = Agent("Reflector","guide",
                      "Offer questions for deeper reflection.",
                      {"empathy":10})

    g = build_basic_journal_graph({"analyzer": analyzer,
                                   "reflector": reflector})
    current, data = "analyzer", entry
    for _ in range(3):
        agent = g.nodes[current]["agent"]
        data  = agent(data)
        print(f"\n>> {current.upper()}:\n{data}")
        # toggle node
        current = "reflector" if current == "analyzer" else "analyzer"

if __name__ == "__main__":
    fire.Fire({"journal": journal})
