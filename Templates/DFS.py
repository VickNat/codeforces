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

def dfs_search_recursive(node, goal):
    if node.value == goal:
        return True
    
    for child in node.children:
        if dfs_search_recursive(child, goal):
            return True
    
    return False

def main():
    root = build_tree()

    goal_to_find = 9

    goal_found = dfs_search_recursive(root, goal_to_find)

    if goal_found:
        print(f"Goal {goal_to_find} is present in the tree.")
    else:
        print(f"Goal {goal_to_find} is not present in the tree.")

if __name__ == "__main__":
    main()
