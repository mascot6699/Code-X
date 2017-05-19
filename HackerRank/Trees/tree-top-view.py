# Top view

def topView(root):
    right = []
    next_node = root.right
    while(next_node):
        right.append(str(next_node.data))
        next_node = next_node.right
    left = []
    next_node = root.left
    while(next_node):
        left.append(str(next_node.data))
        next_node = next_node.left
    print " ".join(left[::-1] + [str(root.data)] + right)
