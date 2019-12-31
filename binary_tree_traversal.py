class NodeAssign:
    # Constructor
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val 

class MakeTree:
    # Constructor
    def __init__(self):
        self.count = 0
    
    def node_insert(self, data, node):
        if node is None:
            return NodeAssign(data)
            self.count += 1
        elif self.count % 2 != 0: 
            node.left = self.node_insert(data, node.left)
            self.count += 1
        elif self.count % 2 == 0:
            node.right = self.node_insert(data, node.right)
            self.count += 1
        else:
            pass
        return node

    # Pre-order traversal
    # Root - Left - Right   
    def pre_order(self,root):
        if root is not None:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)   

    # In-order traversal
    # Left - Root - Right 
    def in_order(self,root):    
        if root is not None:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    # Post-order traversal
    # Left - Right - Root 
    def post_order(self,root):
        if root is not None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)

def operation():
    root = None
    tree = MakeTree()
    root = tree.node_insert(10,root)
    # print(root.data)
    tree.node_insert(20,root)
    tree.node_insert(30,root)
    tree.node_insert(40,root)
    tree.node_insert(70,root)
    tree.node_insert(60,root)
    tree.node_insert(80,root)

    print("Traverse Inorder")
    tree.in_order(root)

    print("Traverse Preorder")
    tree.pre_order(root)

    print("Traverse Postorder")
    tree.post_order(root)


if __name__ == "__main__":
    operation()

