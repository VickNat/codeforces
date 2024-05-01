class Node:
    def __init__(self, value, cost):
        self.value = value
        self.cost = cost
        self.children = []

def build_tree():
    # Create nodes
    root = Node(1, 0)
    node2 = Node(2, 3)
    node3 = Node(3, 2)
    node4 = Node(4, 5)
    node5 = Node(5, 4)
    node6 = Node(6, 1)
    
    # Build the tree structure
    root.children = [(node2, node2.cost), (node3, node3.cost)]
    node2.children = [(node4, node4.cost), (node5, node5.cost)]
    node3.children = [(node6, node6.cost)]

    return root

def ucs_search(root, goal):
    if root.value == goal:
        return True
    
    queue = [(root, 0)]  # (Node, cumulative cost)
    while queue:
        queue.sort(key=lambda x: x[1])  # Sort by cumulative cost
        current, cumulative_cost = queue.pop(0)
        
        if current.value == goal:
            return True
        
        for child, cost in current.children:
            queue.append((child, cumulative_cost + cost))
    
    return False

def main():
    # Build a simple tree
    root = build_tree()

    # Define a goal to search for
    goal_to_find = 9

    # Perform Uniform Cost Search
    goal_found = ucs_search(root, goal_to_find)

    # Display result
    if goal_found:
        print(f"Goal {goal_to_find} is present in the tree using Uniform Cost Search.")
    else:
        print(f"Goal {goal_to_find} is not present in the tree using Uniform Cost Search.")

if __name__ == "__main__":
    main()
