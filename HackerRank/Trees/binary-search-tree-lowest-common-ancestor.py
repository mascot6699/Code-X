# recursive
def lca(root , v1 , v2):
    if v1 < root.data and v2 < root.data:
        return lca(root.left, v1, v2)
    elif v1 > root.data and v2 > root.data:
        return lca(root.right, v1, v2)
    return root


# iterative solution
def lca(root , v1 , v2):
    while(v1 < root.data and v2 < root.data):
        root = root.left
    while(v1 > root.data and v2 > root.data):
        root = root.right
    return root
