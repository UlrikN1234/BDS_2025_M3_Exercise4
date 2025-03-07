# app.py
# A FastAPI backend made to handle requests from the frontend

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize the DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

# Define request and response schemas
class CrewRequest(BaseModel):
    var1: str
    var2: str
    var3: str

class CrewResponse(BaseModel):
    result: str

# Initialize FastAPI app
app = FastAPI(
    title="Crew AI API",
    description="API for running custom Crew AI tasks",
    version="1.0.0",
)

# Define the CustomCrew class
class CustomCrew:
    def __init__(self, var1: str, var2: str, var3: str):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def run(self) -> dict:
        agents = CustomAgents()
        tasks = CustomTasks()

        # Initialize custom agents
        agent1 = agents.agent_1_business_strategist()
        agent2 = agents.agent_2_corporate_financial_planner()
        agent3 = agents.agent_3_market_researcher()
        agent4 = agents.agent_4_operations_manager()
        agent5 = agents.agent_5_marketing_expert()
        agent6 = agents.agent_6_human_resources_specialist()
        agent7 = agents.agent_7_legal_advisor()
        agent8 = agents.agent_8_technology_expert()
        agent9 = agents.agent_9_business_plan_expert()


        # Initialize custom tasks
        task1 = tasks.task_1_business_strategist(agent1, self.var2)
        task2 = tasks.task_2_corporate_financial_planner(agent2, self.var2)
        task3 = tasks.task_3_market_researcher(agent3, self.var1, self.var2, self.var3)
        task4 = tasks.task_4_operations_manager(agent4, self.var1, self.var2)
        task5 = tasks.task_5_marketing_expert(agent5, self.var1, self.var2, self.var3)
        task6 = tasks.task_6_human_resources_specialist(agent6, self.var1)
        task7 = tasks.task_7_legal_advisor(agent7, self.var1)  
        task8 = tasks.task_8_technology_expert(agent8, self.var1)
        task9 = tasks.task_9_business_plan_expert(agent9, self.var1)

        # Create and run the crew
        crew = Crew(
            agents=[agent1, agent2, agent3, agent4, agent5, agent6, agent7, agent8, agent9],
            tasks=[task1, task2, task3, task4, task5, task6, task7, task8, task9],
            verbose=True,
        )
        crew_output = crew.kickoff()

        return {"output": getattr(crew_output, 'raw', str(crew_output))}

# Define the API endpoint
@app.post("/run_agents", response_model=CrewResponse)
async def run_crew(crew_request: CrewRequest):
    """
    Run the custom Crew AI with provided variables.

    - **var1**: Business Name(e.g., Thisguys Moneylaundering)
    - **var2**: Business Idea(e.g., Moneylaundering without getting caught with an environmentally conscious agenda)
    - **var3**: Business Vision (e.g., Being the best and most renowned environmentally conscious moneylaundering company)
    """
    try:
        custom_crew = CustomCrew(crew_request.var1, crew_request.var2, crew_request.var3)
        result = custom_crew.run()
        return CrewResponse(result=result["output"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint for health check
@app.get("/")
def read_root():
    return {"message": "Welcome to the Crew AI API. Use /docs for API documentation."}

# Entry point for running the app
if __name__ == "__main__":
    uvicorn.run("your_module_name:app", host="127.0.0.1", port=8000, reload=True)