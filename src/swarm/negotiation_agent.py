import random

class NegotiationAgent:
    """
    Represents an agent in a swarm capable of negotiating for tasks.
    Each agent evaluates tasks based on its preferences and resource constraints.
    """
    def __init__(self, agent_id, capabilities, resource_capacity):
        self.agent_id = agent_id
        self.capabilities = capabilities  # Set of tasks this agent can perform
        self.resource_capacity = resource_capacity  # Total available resource
        self.current_tasks = {}
        self.state = "idle"

    def evaluate_task(self, task):
        """
        Evaluate a task based on its priority and required resources.
        """
        if task["type"] not in self.capabilities:
            print(f"Agent {self.agent_id} cannot perform task {task['id']}.")
            return 0  # Can't perform this task

        if self.resource_capacity < task["resource_cost"]:
            print(f"Agent {self.agent_id} lacks resources for task {task['id']}.")
            return 0  # Insufficient resources

        score = task["priority"] - task["resource_cost"] / self.resource_capacity
        print(f"Agent {self.agent_id} evaluated task {task['id']} with score {score:.2f}.")
        return score

    def bid_for_task(self, task, marketplace):
        """
        Submit a bid for a task to the marketplace.
        """
        bid_score = self.evaluate_task(task)
        if bid_score > 0:
            print(f"Agent {self.agent_id} submits a bid for task {task['id']} with score {bid_score:.2f}.")
            marketplace.receive_bid(self, task["id"], bid_score)

    def perform_task(self, task):
        """
        Perform a task and consume resources.
        """
        if self.resource_capacity >= task["resource_cost"]:
            self.resource_capacity -= task["resource_cost"]
            self.current_tasks[task["id"]] = task
            self.state = "working"
            print(f"Agent {self.agent_id} is now performing task {task['id']}.")

    def complete_task(self, task_id):
        """
        Complete a task and release resources.
        """
        if task_id in self.current_tasks:
            print(f"Agent {self.agent_id} has completed task {task_id}.")
            del self.current_tasks[task_id]
            self.state = "idle"