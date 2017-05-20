import queue

def levelOrder(root):
    q = queue.Queue()
    q.put(root)
    while(not q.empty()):
        node = q.get()
        print("{} -> ".format(node.data))
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
