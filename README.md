# Noor 🤍: Your Agentic AI Lifestyle Architect

**Noor** (meaning *Light/Glow*) is a stateful, multi-agent AI companion designed to help users balance Mind, Body, and Soul. Built using **LangGraph** and **Llama 3.3 (Groq)**, Noor isn't just a chatbot—it's a system of expert agents that remember your journey and help you build a 1% better life every day.

## 🚀 Core Features

### 1. 🧠 Multi-Agent Orchestration (LangGraph)
Noor uses a **Supervisor-Worker** architecture. A central Supervisor node analyzes user intent and routes the conversation to the specialized expert:
- **🧘‍♀️ The Therapist:** Provides CBT-based emotional support and grounding exercises.
- **⚡ The Habit Coach:** Focuses on discipline, tracking the "Core 4" pillars (Body, Mind, Soul, Space), and the "2-Minute Rule."
- **🛡️ The Safety Agent:** A high-priority filter for crisis intervention and risk assessment.

### 2. 💾 Persistent Memory
Unlike standard chatbots, Noor has a "Brain Upgrade" using **SQLite persistence**. It remembers your name, your past wins, and your specific goals even after a system restart.

### 3. ⚖️ Triage & Hyperbole Filtering
The system includes custom logic to distinguish between casual hyperbole (e.g., "This assignment is killing me") and actual safety risks, ensuring empathetic but responsible support.

## 🛠️ Tech Stack
- **Framework:** LangGraph (Stateful Multi-Agent Orchestration)
- **LLM:** Llama-3.3-70b via Groq API
- **Memory:** SQLite (SqliteSaver) for long-term state management
- **Environment:** Python 3.12, venv, python-dotenv

## 📐 Architecture Topology

## 🎯 Project Background
Developed as part of my journey in **M.Sc. Data Science at VIT**, Noor represents a shift toward "Agentic AI"—systems that don't just respond, but act with intention, character, and integrity.

---
*"Discipline is the highest form of self-love." — Noor 🤍*
