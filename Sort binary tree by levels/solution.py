from collections import deque

class Node:
    def __init__(self, data, left = None, right = None):
        self.value = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value}'


def tree_by_levels(node):
    if not node:
        return
    output = []
    queue = deque()
    queue.append(node)
    current_node = node
    c = False
    while True:
        current_node = queue.popleft()
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        output.append(current_node.value)
        # current_node = queue.popleft()
        if not queue:
            break
    return output
  
print(tree_by_levels(Node(1, Node(2, Node(4)), Node(3))))