from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        db=db,
        markdown=True,
        add_history_to_context=True,
        enable_user_memories=True
    )

user_id = "god_1"
groq_agent = build_agent()
groq_agent.print_response("what is capital of India?", user_id=user_id)
groq_agent.print_response("Is it safe to visit it?", user_id=user_id)

memories = groq_agent.get_user_memories(user_id=user_id)

print("Memories:")
pprint(memories)

