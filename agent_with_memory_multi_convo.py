from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

llm = OpenAIChat(id="gpt-4.1-mini")

user_id= "user1"

db=SqliteDb(db_file="chat_history_multi_convo.db")