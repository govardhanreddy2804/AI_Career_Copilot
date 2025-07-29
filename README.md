# 🤖 AI Career Copilot

A smart assistant that helps you analyze resumes, identify skill gaps, generate personalized cover letters, and create customized learning paths using LLMs and LangChain Agents.

## 🚀 Features

- 📄 Resume and Job Description Input
- 🧠 Skill Gap Analysis
- ✍️ AI-Generated Cover Letters
- 🎯 Personalized 30-Day Learning Plan
- 🧰 Built with Streamlit, OpenAI/Groq, LangChain, and ChromaDB
- 🧠 Supports Agentic AI and RAG (Retrieval-Augmented Generation)

## 📁 Project Structure

AI_Career_Copilot/
│
├── agents/ # Contains learning_path_agent.py, resume_agent.py, tools.py
├── ui/ # Streamlit front-end interface
├── rag/ # RAG implementation files (upcoming)
├── data/ # Upload folders (e.g., resumes/)
├── .env # API keys (excluded from Git)
├── requirements.txt # Python dependencies
├── app.py # Entry point (optional)
└── README.md # Project overview (this file)


## 💻 Setup Instructions

```bash
git clone https://github.com/govardhanreddy2804/AI_Career_Copilot.git
cd AI_Career_Copilot

# Set up a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run ui/streamlit_ui.py

#🤝 Contributions
Pull requests are welcome. For major changes, please open an issue first.

---





