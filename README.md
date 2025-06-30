# Agentic Knowledge Graph Starter

## Build local-first cognitive systems with Ollama + NetworkX + ChromaDB

Why?

LLMs are brilliant but forgetful. This repo turns them into agents with memory and structure, exactly as detailed in the book Building Agentic Knowledge Graphs with Local LLMs.

## Features
	•	🧠 Agents as code – reusable Python classes with traits & memory
	•	🕸️ Graph orchestration – NetworkX wires tasks, feedback and routing
	•	💾 Vector memory – ChromaDB stores journal entries, Reddit threads…
	•	🔍 Fully local – no API keys, no cloud, just Ollama-served models
	•	⚡ Quick demos – try python run.py journal "I feel stuck" in 30 s

## Quick Start

git clone https://github.com/kliewerdaniel/agentic-kg-starter.git
cd agentic-kg-starter
pip install -r requirements.txt
ollama pull mistral   # or your favourite model in another terminal
python run.py journal "I feel stuck but hopeful."

## Extend
	•	Add new agents in src/agents.py
	•	Define bigger graphs in src/graph_builder.py
	•	Store & load graph templates (.yaml coming soon)
	•	Spin up streamlit run Ui/streamlit_app.py to see your graph evolve.

💡 Like the concept? The full 70-page guide dives deep into advanced patterns (temporal memory, self-evolving agents, UI recipes). Grab it here.
https://6340588028610.gumroad.com/l/ddsrtm
