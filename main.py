import os
from PIL import Image
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import VisionTool
from dotenv import load_dotenv
from IPython.display import display, Markdown

# Load the environment variables
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if api_key is None:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = api_key

# Import the LLM class from the CrewAI library
llm = LLM(
    model="gpt-4o",
    temperature=0.8
)

# Set the path to the image file
image_path = "image1.png"

# Open the image using PIL
image = Image.open(image_path)

# Initialize the VisionTool
vision_tool = VisionTool()

# First Agent: Image Analyzer
image_analyzer_agent = Agent(
    role="Image Describer",
    goal=f"Describe the content of the image {image_path} accurately and comprehensively.",
    backstory="Expert Designer working for a B2B Restaurant Startup.",
    verbose=True,
    tools=[vision_tool],
    llm=llm
)

# Assuming 'image1.png' is the path to your image
task_describe_image = Task(
    description="Describe the content of the image.",
    expected_output="A detailed description of the image",
    agent=image_analyzer_agent
)

# Second Agent: Design Improvement Suggestion Agent
designer_agent = Agent(
    role="Design Improvement Suggestion Agent",
    goal=f"Review image descriptions and provide actionable improvement suggestions to the described scene {image_path}.",
    backstory="You are an expert designer with a keen eye for detail, specializing in B2B restaurant design.",
    verbose=True,
    llm=llm,
    tools=[vision_tool]
)

task_suggest_improvements = Task(
    description="Review the image description and suggest improvements to the image. Focus on design and visual elements.",
    expected_output="A list of actionable suggestions.",
    agent=designer_agent,
    context=[task_describe_image]
)

# Third Agent: Product Manager
product_manager_agent = Agent(
    role="Product Manager",
    goal=f"Create user stories and prioritize them based on the image {image_path}.",
    backstory="You are a product manager experienced in B2B restaurant solutions.",
    verbose=True,
    llm=llm,
    tools=[vision_tool]
)

task_create_user_stories = Task(
    description="Create user stories based on the design improvements suggested. Prioritize these user stories based on impact and feasibility.",
    expected_output="A prioritized list of user stories.",
    agent=product_manager_agent,
    context=[task_describe_image, task_suggest_improvements]
)

# Assemble the crew
ai_team = Crew(
    agents=[image_analyzer_agent, designer_agent, product_manager_agent],
    tasks=[task_describe_image, task_suggest_improvements, task_create_user_stories],
    process=Process.sequential,
    verbose=True
)

# Execute the crew
result = ai_team.kickoff()

# Write the output to a Markdown file
with open("output.md", "a") as md_file:
    md_file.write("## Crew Execution Results in Markdown:\n")

    for idx, task_output in enumerate(result.tasks_output):
      display(Markdown(f"Agent {idx + 1}: {task_output.agent}\n{task_output.raw}"))