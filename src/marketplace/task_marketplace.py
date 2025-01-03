class TaskMarketplace:
    """
    A decentralized marketplace for task negotiation between agents.
    Agents bid for tasks, and the marketplace assigns tasks to the highest bidder.
    """
    def __init__(self):
        self.tasks = []
        self.bids = {}  # Maps task_id to a list of (agent, bid_score)

    def add_task(self, task):
        """
        Add a new task to the marketplace.
        """
        self.tasks.append(task)
        self.bids[task["id"]] = []
        print(f"Task {task['id']} added to the marketplace.")

    def receive_bid(self, agent, task_id, bid_score):
        """
        Receive a bid from an agent for a specific task.
        """
        self.bids[task_id].append((agent, bid_score))
        print(f"Marketplace received a bid for task {task_id} from Agent {agent.agent_id} with score {bid_score:.2f}.")

    def assign_tasks(self):
        """
        Assign tasks to the highest bidding agents.
        """
        for task_id, bid_list in self.bids.items():
            if not bid_list:
                print(f"No bids received for task {task_id}.")
                continue

            # Find the highest bidder
            bid_list.sort(key=lambda x: x[1], reverse=True)
            winner, _ = bid_list[0]

            # Assign task to the winning agent
            task = next(t for t in self.tasks if t["id"] == task_id)
            print(f"Task {task_id} assigned to Agent {winner.agent_id}.")
            winner.perform_task(task)

        # Clear bids after assignment
        self.bids.clear()