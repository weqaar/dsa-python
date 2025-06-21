class TreeNode:
    """Represents a node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_preorder(root: TreeNode | None):
    """
    Performs a Depth-First Search (pre-order traversal) on a binary tree
    and prints the value of each node.

    Args:
        root: The root node of the binary tree.
    """
    if root is None:
        return

    # Visit the current node (pre-order: visit, then left, then right)
    print(root.val, end=" ")

    # Traverse the left subtree
    dfs_preorder(root.left)

    # Traverse the right subtree
    dfs_preorder(root.right)

def dfs_inorder(root):
    if root is None: return
    dfs_inorder(root.left)
    print(root.val, end=" ") # Visit in the middle
    dfs_inorder(root.right)

def dfs_postorder(root):
    if root is None: return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.val, end=" ") # Visit at the end

# --- Example Usage ---

# Construct a sample binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("DFS (Pre-order traversal):")
dfs_preorder(root)
print("\n") # Add a newline at the end

# Another example tree:
#       10
#      /
#     5
#      \
#       7
#      /
#     6
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.left.right = TreeNode(7)
root2.left.right.left = TreeNode(6)

print("DFS (Pre-order traversal) for second tree:")
dfs_preorder(root2)
print("\n")

