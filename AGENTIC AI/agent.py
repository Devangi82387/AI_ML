from agno.agent import Agent
from agno.models.groq import Groq
import google.generativeai as genai

from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv
load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )

groq_agent = build_agent()
groq_agent.print_response("Is it safe to travel UAE today?")
