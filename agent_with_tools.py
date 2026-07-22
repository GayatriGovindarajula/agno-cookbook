from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

llm = OpenAIChat(id="gpt-4.1-mini")

web_search = DuckDuckGoTools()

agent = Agent(
    name= "agent_with_web_search",
    tools=[web_search],
    instructions="you are an expert in searching web. you have access to web search tool to get the latest information",
    model=llm,
    stream=True,
    markdown=True
)

agent.print_response("Get me some happy news about today?")