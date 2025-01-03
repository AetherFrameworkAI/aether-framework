import random
from collections import defaultdict

class NeuralAgent:
    """
    Base class for a neural agent that operates within a hierarchical system.
    Implements a simulated neural network decision process.
    """
    def __init__(self, agent_id, layer):
        self.agent_id = agent_id
        self.layer = layer  # Hierarchy level
        self.local_weights = [random.random() for _ in range(5)]  # Simulated neural weights
        self.input_cache = []
        self.state = "idle"
        self.output_signal = None

    def process_input(self, input_data):
        """
        Processes input data through simulated neural computation.
        """
        self.input_cache.append(input_data)
        weighted_sum = sum(w * i for w, i in zip(self.local_weights, input_data))
        self.output_signal = 1 / (1 + 2.718 ** -weighted_sum)  # Sigmoid activation
        print(f"Agent {self.agent_id} at layer {self.layer} processed input into output: {self.output_signal:.4f}")

    def send_signal(self, higher_agent):
        """
        Sends processed signals to a higher-level agent.
        """
        if higher_agent:
            print(f"Agent {self.agent_id} sends signal to Agent {higher_agent.agent_id}: {self.output_signal:.4f}")
            higher_agent.receive_signal(self.output_signal)

    def receive_signal(self, signal):
        """
        Receives signals from lower-level agents for hierarchical aggregation.
        """
        print(f"Agent {self.agent_id} at layer {self.layer} received signal: {signal:.4f}")
        self.input_cache.append(signal)


class HierarchicalNeuralSystem:
    """
    A multi-layer hierarchical neural agent system simulating emergent intelligence.
    """
    def __init__(self, num_layers, agents_per_layer):
        self.hierarchy = defaultdict(list)
        self.num_layers = num_layers
        self.agents_per_layer = agents_per_layer

        # Initialize agents per layer
        for layer in range(num_layers):
            self.hierarchy[layer] = [
                NeuralAgent(agent_id=f"{layer}-{i}", layer=layer) for i in range(agents_per_layer)
            ]

    def simulate(self, iterations):
        """
        Simulates the hierarchical communication over a number of iterations.
        """
        for _ in range(iterations):
            print("\n--- Iteration ---")

            # Process input for bottom-layer agents
            for agent in self.hierarchy[0]:
                random_input = [random.random() for _ in range(5)]
                print(f"Feeding random input to Agent {agent.agent_id}: {random_input}")
                agent.process_input(random_input)

            # Propagate signals upwards
            for layer in range(self.num_layers - 1):
                for agent in self.hierarchy[layer]:
                    higher_agents = self.hierarchy[layer + 1]
                    higher_agent = random.choice(higher_agents)
                    agent.send_signal(higher_agent)

            # Simulate top-level decision-making
            top_layer = self.num_layers - 1
            for agent in self.hierarchy[top_layer]:
                print(f"Top-layer Agent {agent.agent_id} is analyzing aggregated signals: {agent.input_cache}")
                agent.make_decision()

    def get_hierarchy_state(self):
        """
        Retrieves the current state of all agents in the hierarchy.
        """
        return {
            layer: [agent.state for agent in agents]
            for layer, agents in self.hierarchy.items()
        }


class DecisionMakingAgent(NeuralAgent):
    """
    Specialized top-level agent that makes a final decision based on aggregated inputs.
    """
    def make_decision(self):
        """
        Aggregates received signals and performs a pseudo-decision process.
        """
        if not self.input_cache:
            print(f"Agent {self.agent_id} has no inputs to process.")
            return

        decision_score = sum(self.input_cache) / len(self.input_cache)
        self.state = "deciding" if decision_score > 0.5 else "idle"
        print(f"Agent {self.agent_id} makes a decision with score {decision_score:.4f}: {self.state}")


# Example usage
if __name__ == "__main__":
    system = HierarchicalNeuralSystem(num_layers=3, agents_per_layer=4)

    # Replace top-layer agents with DecisionMakingAgent
    for i in range(4):
        system.hierarchy[2][i] = DecisionMakingAgent(agent_id=f"2-{i}", layer=2)

    system.simulate(3)  # Simulate for 3 iterations
    print("\nHierarchy State:", system.get_hierarchy_state())