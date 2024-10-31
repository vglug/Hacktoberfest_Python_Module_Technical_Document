class Node:
    """A class representing a single node in a binary tree."""
    
    def __init__(self, key):
        """
        Initialize a new node with the given key.
        
        Parameters:
        key (any): The value to be stored in the node.
        """
        self.left = None  # Initialize left child as None
        self.right = None  # Initialize right child as None
        self.value = key  # Store the value in the node

class BinaryTree:
    """A class representing a binary tree."""
    
    def __init__(self):
        """Initialize the binary tree with a root node set to None."""
        self.root = None  # The root of the tree is initially None

    def insert(self, key):
        """
        Insert a new node with the given key into the binary tree.
        
        Parameters:
        key (any): The value to be inserted into the tree.
        """
        if self.root is None:
            self.root = Node(key)  # If tree is empty, set root to new node
        else:
            self._insert_recursively(self.root, key)  # Otherwise, insert recursively

    def _insert_recursively(self, current_node, key):
        """
        Helper method to insert a new node recursively.
        
        Parameters:
        current_node (Node): The current node in the tree.
        key (any): The value to be inserted into the tree.
        """
        if key < current_node.value:  # If the key is less than the current node's value
            if current_node.left is None:  # If there is no left child
                current_node.left = Node(key)  # Insert new node here
            else:
                self._insert_recursively(current_node.left, key)  # Recur on left child
        else:  # If the key is greater than or equal to the current node's value
            if current_node.right is None:  # If there is no right child
                current_node.right = Node(key)  # Insert new node here
            else:
                self._insert_recursively(current_node.right, key)  # Recur on right child

    def inorder_traversal(self, node):
        """
        Perform an in-order traversal of the tree.
        
        Parameters:
        node (Node): The current node to start the traversal from.
        
        Returns:
        list: A list of values in in-order sequence.
        """
        return (self.inorder_traversal(node.left) + [node.value] + 
                self.inorder_traversal(node.right)) if node else []

    def preorder_traversal(self, node):
        """
        Perform a pre-order traversal of the tree.
        
        Parameters:
        node (Node): The current node to start the traversal from.
        
        Returns:
        list: A list of values in pre-order sequence.
        """
        return ([node.value] + self.preorder_traversal(node.left) + 
                self.preorder_traversal(node.right)) if node else []

    def postorder_traversal(self, node):
        """
        Perform a post-order traversal of the tree.
        
        Parameters:
        node (Node): The current node to start the traversal from.
        
        Returns:
        list: A list of values in post-order sequence.
        """
        return (self.postorder_traversal(node.left) + 
                self.postorder_traversal(node.right) + [node.value]) if node else []

    def search(self, key):
        """
        Search for a node with the given key in the tree.
        
        Parameters:
        key (any): The value to search for in the tree.
        
        Returns:
        bool: True if the key is found, False otherwise.
        """
        return self._search_recursively(self.root, key)

    def _search_recursively(self, current_node, key):
        """
        Helper method to search for a key recursively.
        
        Parameters:
        current_node (Node): The current node in the tree.
        key (any): The value to search for in the tree.
        
        Returns:
        bool: True if the key is found, False otherwise.
        """
        if current_node is None:  # If the current node is None, key is not found
            return False
        if current_node.value == key:  # If the current node's value matches the key
            return True
        elif key < current_node.value:  # If the key is less, search left
            return self._search_recursively(current_node.left, key)
        else:  # If the key is greater, search right
            return self._search_recursively(current_node.right, key)

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    print("In-order traversal:", tree.inorder_traversal(tree.root))  # Output: [5, 10, 15]
    print("Pre-order traversal:", tree.preorder_traversal(tree.root))  # Output: [10, 5, 15]
    print("Post-order traversal:", tree.postorder_traversal(tree.root))  # Output: [5, 15, 10]
    print("Search for 15:", tree.search(15))  # Output: True
    print("Search for 20:", tree.search(20))  # Output: False


# 1. Node Class: Represents a single node in the binary tree. It has a value and pointers to its left and right children.
# 2. BinaryTree Class: Represents the binary tree itself. It has methods for inserting nodes, traversing the tree, and searching for values.
# 3. Insert Method: Adds a new node to the tree. If the tree is empty, it sets the root. Otherwise, it calls a helper method to find the correct position for the new node.
# 4. Traversal Methods: Implement in-order, pre-order, and post-order traversals, which are common ways to visit all nodes in a tree.
# 5. Search Method: Looks for a specific value in the tree, returning True if found and False otherwise.