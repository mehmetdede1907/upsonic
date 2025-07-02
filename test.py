from upsonic import Task, Agent

# String as Context
city = "New York"


# Creating Task
task = Task(
  "Find eating places in the city",
  context=[city] # Adding city string as context
)

# Creating Agent
agent = Agent(name="City Guide")

# Running the task
agent.print_do(task)