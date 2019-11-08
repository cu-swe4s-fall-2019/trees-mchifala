dclass Node:
    """
    This class serves as the nodes of a tree.
    
    Attributes:
    - left(Node): the left child of the node
    - right(Node): the right child of the node
    - key(int): the key of the node
    - value(varies): the value of the node

    """
    def __init__(self, key, value=None, left=None, right=None):
        """
        This constructor initializes the node
        """
        self.left = None
        self.right = None
        self.key = key
        self.value  = value

def insert(root, key, value=None):
    new_node = Node(key, value)
    if root is None:
        root = new_node
    else:
        insert_helper(root, new_node)

def insert_helper(root, node):
    if root is None:
        root = node
    elif root.key < node.key:
        if root.right is None:
            root.right = node
        else:
            insert_helper(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert_helper(root.left, node)
        
def search(root, key):
    while root is not None and key != root.key:
        if key < root.key:
            root = root.left
        else:
            root = root.right
            
    return root.value
