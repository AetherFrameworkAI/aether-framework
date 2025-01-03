import random
from collections import defaultdict

class CognitiveNode:
    """
    Represents a single node capable of decentralized cognitive processing and coordination.
    Each node operates autonomously but contributes to collective problem-solving.
    """
    def __init__(self, node_id):
        self.node_id = node_id
        self.knowledge_base = defaultdict(float)  # Shared knowledge as a weighted map
        self.active_tasks = []  # Tasks currently assigned to the node
        self.state = "idle"

    def contribute_knowledge(self, task_id, contribution):
        """
        Nodes contribute knowledge updates to shared tasks in the system.
        """
        self.knowledge_base[task_id] += contribution
        print(f"Node {self.node_id} contributed {contribution:.2f} to task {task_id}.")

    def process_task(self, task_id):
        """
        Perform a task, generating knowledge contributions based on a random factor.
        """
        if self.state != "idle":
            print(f"Node {self.node_id} is busy and cannot process new tasks.")
            return
        
        self.state = "processing"
        contribution = random.uniform(0.1, 1.0)  # Simulated task contribution
        print(f"Node {self.node_id} is processing task {task_id} with contribution {contribution:.2f}.")
        self.contribute_knowledge(task_id, contribution)
        self.state = "idle"

    def share_knowledge(self, other_node):
        """
        Share a portion of the knowledge base with another node.
        """
        shared_task = random.choice(list(self.knowledge_base.keys()))
        shared_value = self.knowledge_base[shared_task] * 0.5  # Share 50% of the value
        print(f"Node {self.node_id} shares {shared_value:.2f} of task {shared_task} with Node {other_node.node_id}.")
        other_node.receive_knowledge(shared_task, shared_value)

    def receive_knowledge(self, task_id, value):
        """
        Receive a knowledge update from another node.
        """
        print(f"Node {self.node_id} received {value:.2f} knowledge for task {task_id}.")
        self.knowledge_base[task_id] += value


class DecentralizedCognitiveSystem:
    """
    A decentralized system of cognitive nodes designed for task coordination and collective learning.
    """
    def __init__(self, node_count):
        self.nodes = [CognitiveNode(node_id=i) for i in range(node_count)]
        self.tasks = defaultdict(list)  # Tasks and assigned nodes

    def assign_task(self, task_id, node):
        """
        Assign a task to a specific node.
        """
        if node.state != "idle":
            print(f"Node {node.node_id} is busy and cannot take new tasks.")
            return
        print(f"Assigning task {task_id} to Node {node.node_id}.")
        node.active_tasks.append(task_id)
        self.tasks[task_id].append(node)

    def simulate(self, iterations):
        """
        Simulates the system over multiple iterations.
        """
        for _ in range(iterations):
            print("\n--- Iteration ---")
            # Randomly assign tasks
            for _ in range(len(self.nodes) // 2):  # Assign tasks to half the nodes
                task_id = random.randint(0, 10)
                node = random.choice(self.nodes)
                self.assign_task(task_id, node)
                node.process_task(task_id)

            # Randomly share knowledge
            for _ in range(len(self.nodes) // 3):  # Share knowledge among a subset of nodes
                node1, node2 = random.sample(self.nodes, 2)
                node1.share_knowledge(node2)

    def get_system_state(self):
        """
        Retrieves the collective knowledge base and node states.
        """
        knowledge_summary = {node.node_id: dict(node.knowledge_base) for node in self.nodes}
        return {
            "knowledge_summary": knowledge_summary,
            "node_states": {node.node_id: node.state for node in self.nodes},
        }


# Example Usage
if __name__ == "__main__":
    system = DecentralizedCognitiveSystem(node_count=5)
    system.simulate(iterations=5)

    print("\nSystem State:")
    print(system.get_system_state())