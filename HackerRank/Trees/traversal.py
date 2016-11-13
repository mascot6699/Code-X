class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "Preorder traversal of binary tree is\n"
preOrder(root)
 
print "\nInorder traversal of binary tree is\n"
inOrder(root)
 
print "\nPostorder traversal of binary tree is\n"
postOrder(root)