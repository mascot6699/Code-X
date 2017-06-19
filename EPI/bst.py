# Inorder traversal iterative. s is used as a stack.
def bst_in_sorted_order(tree):
    s, result = [], []
    while s or tree:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            result.append(tree.data)
            tree = tree.right
    return result

# Preorder traversal. path is used as a stack
def preorder_traversal(tree):
    path, result = [tree], []
    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right, curr.left]
    return result

# left-most node of the right subtree if present or 
# parent whose node is left child of self
def find_successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node.parent.right is node:
        node = node.parent
    return node.parent


def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))