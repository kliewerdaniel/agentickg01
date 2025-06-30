import networkx as nx

def build_basic_journal_graph(agents: dict):
    g = nx.DiGraph()
    g.add_node("analyzer",   agent=agents["analyzer"])
    g.add_node("reflector",  agent=agents["reflector"])
    g.add_edge("analyzer", "reflector")          # sequential
    g.add_edge("reflector", "analyzer")          # feedback loop
    return g
