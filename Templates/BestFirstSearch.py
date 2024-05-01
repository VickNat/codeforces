from queue import PriorityQueue

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree():
    # Create nodes
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    
    # Build the tree structure
    root.children = [node2, node3]
    node2.children = [node4, node5]
    node3.children = [node6]

    return root

def best_first_search(root, goal):
    if root.value == goal:
        return True
    
    pq = PriorityQueue()
    pq.put((root.value, root))

    while not pq.empty():
        current_value, current_node = pq.get()

        if current_node.value == goal:
            return True
        
        for child in current_node.children:
            pq.put((child.value, child))
    
    return False

def main():
    # Build a simple tree
    root = build_tree()

    # Define a goal to search for
    goal_to_find = 9

    # Perform Best-First Search
    goal_found = best_first_search(root, goal_to_find)

    # Display result
    if goal_found:
        print(f"Goal {goal_to_find} is present in the tree using Best-First Search.")
    else:
        print(f"Goal {goal_to_find} is not present in the tree using Best-First Search.")

if __name__ == "__main__":
    main()
