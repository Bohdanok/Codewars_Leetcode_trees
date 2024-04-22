# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    output = []
    def get_node(head):
        if not head:
            return
        output.append(head.data)
        get_node(head.left)
        get_node(head.right)
    get_node(node)
    return output


# In-order traversal
def in_order(node):
    if node is None:
        return []
    output = []
    def get_node(head):
        if not head:
            return
        get_node(head.left)
        output.append(head.data)
        get_node(head.right)
    get_node(node)
    return output

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    output = []
    def get_node(head):
        if not head:
            return
        get_node(head.left)
        get_node(head.right)
        output.append(head.data)
    get_node(node)
    return output

