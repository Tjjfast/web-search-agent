from agno.models.google import Gemini
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv 

load_dotenv() 

web_searcher = Agent(
    name='Web Search Agent',
    model = Gemini(id='gemini-1.5-flash', api_key = os.getenv('GOOGLE_API_KEY')),
    description='An agent that can search the web and news from the web',
    system_message='reply in one sentence.',
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    debug_mode=True,
    markdown=True,
)

response = web_searcher.run("Give me one headline about AI from the last 24 hours.")
print(response.content)
