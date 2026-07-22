from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

llm=OpenAIChat(id="gpt-4.1-mini")

session_id="session_123"

db=SqliteDb(db_file="qgent_with_sqlite_memory.db")

agent=Agent(
    model=llm,
    db=db,
    name="agent_with_sqlite_memory",
    session_id=session_id,
    add_history_to_context=True,
    num_history_runs=10,
    stream=True,
    markdown=True
)

#agent.print_response(input="Hi, my name is Sakura")
#agent.print_response(input="can you tell me my name? is my name a popular anime character?")
#agent.print_response(input="what is the punch line for sakura's character in naruto?")
#agent.print_response(input="Sakura and I share one physical characteristic in common, a humoungous forhead,hahaha")
agent.print_response(input="can you tell me, what do i share in common with sakura?",session_id=session_id)

messages=agent.get_chat_history(session_id)

for messages in messages:
    role, content = messages.role, messages.content
    if role=="system":
        continue
    else:
        print(f"Role : {role}, Message: {content}")


