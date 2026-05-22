from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from bedrock_agentcore.runtime import BedrockAgentCoreApp
import os

# ---------------------------------------------------
# Initialize Bedrock AgentCore App
# ---------------------------------------------------
app = BedrockAgentCoreApp()

# ---------------------------------------------------
# Initialize Bedrock LLM
# ---------------------------------------------------
bedrock_llm = LLM(
    model="bedrock/us.amazon.nova-pro-v1:0",
    region_name="us-west-2"
)

# ---------------------------------------------------
# Initialize Serper Tool
# ---------------------------------------------------
serper_dev_tool = SerperDevTool(
    api_key=os.environ.get("SERPER_API_Key")
)

# ---------------------------------------------------
# Crew Definition
# ---------------------------------------------------
@CrewBase
class VacationPlanner:
    """Vacation Planner Crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # ---------------------------------------------------
    # Agents
    # ---------------------------------------------------
    @agent
    def vacation_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["vacation_researcher"],
            verbose=True,
            llm=bedrock_llm,
            tools=[serper_dev_tool],
        )

    @agent
    def itinerary_planner(self) -> Agent:
        return Agent(
            config=self.agents_config["itinerary_planner"],
            verbose=True,
            llm=bedrock_llm,
        )

    # ---------------------------------------------------
    # Tasks
    # ---------------------------------------------------
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],
            output_file="report.md",
        )

    # ---------------------------------------------------
    # Crew
    # ---------------------------------------------------
    @crew
    def crew(self) -> Crew:
        """Creates the Vacation Planner Crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            llm=bedrock_llm,
        )

# ---------------------------------------------------
# AgentCore Runtime Entrypoint
# ---------------------------------------------------
@app.entrypoint
def invoke(payload: dict) -> dict:
    topic = payload.get("topic", "")

    result = VacationPlanner().crew().kickoff(
        inputs={"topic": topic}
    )

    return {
        "result": result.raw
    }

# ---------------------------------------------------
# Run Application
# ---------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)