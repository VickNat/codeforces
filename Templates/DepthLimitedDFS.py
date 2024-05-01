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
    root = build_tree()

    goal_to_find = 9
    depth_limit = 2

    goal_found = dldfs_search(root, goal_to_find, depth_limit)

    if goal_found:
        print(f"Goal {goal_to_find} is present in the tree within the depth limit.")
    else:
        print(f"Goal {goal_to_find} is not present in the tree within the depth limit.")

if __name__ == "__main__":
    main()
