from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

db= SqliteDb(db_file="session_state_db/shopping.db")

session_id="2"
user_id="user_a"

llm=OpenAIChat(id="gpt-4.1-mini")

state={"shopping_list":[]}

def add_item(item) -> str:
    """Add an item to the shopping list"""
    item = item.lower()
    if item in state["shopping_list"]:
        return f"{item} already in shopping list"
    else:
        state["shopping_list"].append(item)
        return f"{item} added to the shopping list. The shopping list is now {state['shopping_list']}"

def remove_item(item) -> str:
    """Remove an item from the shopping list for the items I have already purchased, or asked to be removed from the list"""
    item=item.lower()
    if item not in state["shopping_list"]:
        return f"{item} not in shopping list"
    else:
        state["shopping_list"].remove(item)
        return f"{item} removed from the shopping list. The shopping list is now {state['shopping_list']}"

def list_item()->str:
    """list down all the items in shopping list"""
    shopping_list =state["shopping_list"]
    if shopping_list:
        list_of_items = "\n".join([f"- {item}" for item in shopping_list])
        return f"The shopping list is: {list_of_items}"
    else:
        return "The shopping list is empty"

def clear_list()->str:
    """Clears the shopping list of all items and gives you empty list"""
    state["shopping_list"]=[]
    return f"Cleared the shopping list of all the items. The shopping list is {state['shopping_list']}"

agent = Agent(
    model=llm,
    name="agent_with_state",
    session_state=state,
    session_id=session_id,
    user_id=user_id,
    instructions= "Your job is to manage shopping lists. You start off with an empty list and you can add item to this list, remove item from the list if I have already bought them, List items in the list of clear the list of all items.",
    tools=[add_item, remove_item, list_item, clear_list],
    db=db,
    stream=True,
    markdown=True
)
agent.print_response("Can you tell me what is on the shopping list")
print(f"The session state is:{agent.session_state}")

agent.print_response("Add milk to the shopping list")
print(f"The session state is:{agent.session_state}")

agent.print_response("Add eggs and bread to my shopping list")
print(f"This session state is:{agent.session_state}")

agent.print_response("I have bought milk and bread")
print(f"The session state is:{agent.session_state}")

agent.print_response("Can you tell me what is on the shopping list")

