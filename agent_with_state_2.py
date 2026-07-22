from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

# load the api keys
load_dotenv()

# build a db
db = SqliteDb(db_file="session_state_db/shopping.db")

# give a session id and user id
session_id = "1"
user_id = "user_a"

# create a model
llm = OpenAIChat(id="gpt-4.1-mini")

state = {"shopping_list":[]}

# define a tool that adds items to shopping list
def add_item(item: str) -> str:
    """Add an item to the shopping list"""
    state["shopping_list"].append(item)
    return f"The shopping list is now {state["shopping_list"]}"


# create the agent
agent = Agent(
    model=llm,
    name="agent_with_state",
    session_state=state,
    session_id=session_id,
    instructions="You are an expert in maintaining shopping lists. You have access to shopping list: {shopping_list}",
    tools=[add_item],
    user_id=user_id,
    db=db,
    stream=True,
    markdown=True
)

agent.print_response("Add milk to the shopping list")
print(f"The session state is: {agent.session_state}")

agent.print_response("Add eggs and bread to my shopping list")
print(f"The session state is: {agent.session_state}")