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

def iddfs_search(root, goal):
    depth_limit = 0
    while depth_limit < 20:
        result = dldfs_search(root, goal, depth_limit)
        if result:
            return True
        depth_limit += 1

def dldfs_search(node, goal, depth_limit):
    return dldfs_recursive(node, goal, depth_limit, 0)

def dldfs_recursive(node, goal, depth_limit, current_depth):
    if current_depth > depth_limit:
        return False

    if node.value == goal:
        return True
    
    if current_depth == depth_limit:
        return False
    
    for child in node.children:
        if dldfs_recursive(child, goal, depth_limit, current_depth + 1):
            return True
    
    return False

def main():
    # Build a simple tree
    root = build_tree()

    # Define a goal to search for
    goal_to_find = 9

    # Perform Iterative Deepening DFS search
    goal_found = iddfs_search(root, goal_to_find)

    # Display result
    if goal_found:
        print(f"Goal {goal_to_find} is present in the tree using Iterative Deepening DFS.")
    else:
        print(f"Goal {goal_to_find} is not present in the tree using Iterative Deepening DFS.")

if __name__ == "__main__":
    main()
