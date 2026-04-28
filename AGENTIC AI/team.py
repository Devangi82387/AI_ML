from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team
from dotenv import load_dotenv
load_dotenv()

eng_agent = Agent(name="English Agent", role="You answer questions in English")
chi_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")
hin_agent = Agent(name="Hindi Agent", role="You answer questions in Hindi")

team = Team(name="Multilingual Team", 
            members=[eng_agent, chi_agent, hin_agent],
            model=Groq(id="llama-3.1-8b-instant"),
            markdown=True,
            show_members_responses=True,
            instructions="All member must answer the question in their respective language and provide a brief explanation of their answer in respective language. Do not call just one agent. Output the response of all agents."
            )



team.print_response("what is capital of India?")
