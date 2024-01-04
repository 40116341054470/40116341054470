class BTnode:
    def __init__(self,data,left = None,right= None):
        self.data = data
        self.Left = left
        self.Right = right

class BTree:
    def __init__(self,root = None):
        self.root = root

    def inorder(self, root):
        if (root == None):
            return
        else:
            inorder(root.left)
            print(root.data)
            inorder(root.right)

    def postorder(self, root):
        if (root == None):
            return
        else:
            postorder(root.left)
            postorder(root.right)
            print(root.data)

            