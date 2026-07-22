from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.json import JsonDb
from dotenv import load_dotenv

load_dotenv()

llm= OpenAIChat(id="gpt-4.1-mini")

session_id="session_1"

db = JsonDb(db_path="chat_history_db",session_table="session_history")

agent = Agent(
    model=llm,
    db= db,
    name= "agent_with_memory",
    session_id=session_id,
    add_history_to_context= True,
    num_history_runs= 10,
    stream= True,
    markdown= True
)

agent.print_response(input="Hi, my name is Gayatri")
agent.print_response(input="tell me a joke, a dad joke")
agent.print_response(input="generate a poem on gardening")
agent.print_response(input="what is my name?")

messages= agent.get_chat_history(session_id)
for message in messages:
    role, content =message.role, message.content
    if role=="system":
        continue
    else:
        print(f"Role :{role}, Message: {content}")