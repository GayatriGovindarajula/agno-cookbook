from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

db = SqliteDb(db_file="session_state_db/temp.db")

session_id = "1"
user_id= "user_a"

llm= OpenAIChat(id="gpt-4.1-mini")

user_info  ={"name": "Rahul", "age":25}

agent = Agent(
    model=llm,
    name="agent_with_state",
    session_state=user_info,
    session_id=session_id,
    user_id=user_id,
    add_session_state_to_context=True,
    db=db,
    stream=True,
    markdown=True
)
agent.print_response(input="Can you tell me my name and age", session_state={"name":"Neha", "age":30})
print(agent.get_session_state(session_id))