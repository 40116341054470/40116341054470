class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None 

    def inorder(root):
        if root is not None:
            inorder(root.left)
            print (root.key, end=" ")
            inorder(root.right) 


    def insert(root, k):
        if root is None:
            return Node(k)
        if k < root.key:
            root.left = insert(root.left, k)
        else:
            root.right = insert(root.right, k)
        return root 

    def search(root, k):
        if root is None or root.key == k :
            return root
        if k > root.key:
            return search(root.right, k)
        return search(root.left, k)
    