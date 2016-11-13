def check_binary_search_tree_(root):
    return check_node(root, -1, 10001)
    
def check_node(node, min, max):
    if not node:
        return True
    if node.data < min or node.data > max:
        return False
    return check_node(node.left, min, node.data-1) and check_node(node.right, node.data+1, max)