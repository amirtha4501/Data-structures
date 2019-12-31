class NodeAssign:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val 

class MakeTree:
    
    def node_insert(self, data, node):
        if node is None:
            return NodeAssign(data)
    
        elif data < node.data: 
            node.left = self.node_insert(data, node.left)
    
        elif data > node.data:
            node.right = self.node_insert(data, node.right)
    
        else:
            pass
        
        return node

    def delete_node(self, data, node):

        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.delete_node(data, node.left)
        
        elif data > node.data:
            node.right = self.delete_node(data, node.right)
        
        # reach to the node that need to delete from BST.
        else: 
            
            if node.left is None and node.right is None:
                node = None 
                # print("NO child")               
            elif node.left == None:
                temp = node.right
                node = None
                # print("no left child")
                # print(temp.data)
                return  temp
            elif node.right == None:
                temp = node.left
                node = None
                # print("no right child")
                # print(temp.data)
                return temp
            elif node.left is not None and node.right is not None:
                templ = node.left
                tempr = node.right
                del node
                return templ
            else:
                pass
        return node


    # Pre-order traversal
    # Root - Left - Right   
    def pre_order(self,root):
        if root:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)   

    # In-order traversal
    # Left - Root - Right 
    def in_order(self,root):    
        if root:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    # Post-order traversal
    # Left - Right - Root 
    def post_order(self,root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)


def operation():
    root = None
    tree = MakeTree()
    root = tree.node_insert(50,root)
    tree.node_insert(20,root)
    tree.node_insert(30,root)
    tree.node_insert(100,root)
    tree.node_insert(150,root)
    tree.node_insert(200,root)
    tree.node_insert(300,root)

    print("Inorder Traversal")
    tree.in_order(root)

    print("Preorder Traversal")
    tree.pre_order(root)

    print("Postorder Traversal")
    tree.post_order(root)

    s = 0
    while s != 9:
        d = int(input("Do you want to delete?\n(yes:1/no:0): "))
        if d == 1:
            ch = int(input("Enter element to delete: "))
            tree.delete_node(ch,root)

            
            print("Inorder Traversal after Deletion")
            tree.in_order(root)

            print("Preorder Traversal after Deletion")
            tree.pre_order(root)

            print("Postorder Traversal after Deletion")
            tree.post_order(root)

        s = int(input("Enter 9 to quit and others to continue "))

if __name__ == "__main__":
    operation()

