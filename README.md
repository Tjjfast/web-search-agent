# Agno Web Search Agent

This project demonstrates a simple AI agent built using the [Agno framework](https://docs.agno.com). The agent uses **Google Gemini** as the LLM and integrates with **DuckDuckGo** tools to fetch real-time web and news data, returning concise one-sentence replies.

---

## Features

-  Real-time web & news search using DuckDuckGo
-  Gemini LLM (`models/gemini-1.5-flash`) for summarizing responses
-  Responds to natural language prompts
-  One-sentence replies via system prompt
-  Debug mode + markdown support enabled

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```
git clone https://github.com/Tjjfast/web-search-agent.git
cd web-search-agent
```
### 2. Create .env File
Create a file named .env in the root directory and add your Gemini API key:
```
GOOGLE_API_KEY="exampleAPIkey"
```
Do not share your API key publicly.
### 3. Install Requirements
```
pip install -r requirements.txt
```
### 4. Run the Agent
```
python agent.py
```
The agent will run a web search query and return a one-line response using Gemini.

### Example Prompt :
```
Give me one headline about AI from the last 24 hours.
```
The agent will fetch relevant web content and return a summarized one-line answer.

### Project Structure :
```
📁 web-search-agent/
├── agent.py              # Main script
├── .env                  # API key 
├── requirements.txt      # Dependencies
└── README.md             # This file
```
### Demo Video :
Watch the demo video [here](https://pages.github.com/)
