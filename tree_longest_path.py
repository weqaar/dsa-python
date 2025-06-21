class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def longest_path(root):
    def dfs(node):
        if not node:
            return 0, 0  # (height, diameter)

        left_height, left_diameter = dfs(node.left)
        right_height, right_diameter = dfs(node.right)

        current_height = 1 + max(left_height, right_height)
        current_diameter = max(
            left_diameter, right_diameter, left_height + right_height
        )

        return current_height, current_diameter

    _, diameter = dfs(root)
    return diameter


# Example usage:
# Constructing the tree from the example
root = TreeNode(2)
root.left = TreeNode(7)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(11)
root.right.right = TreeNode(9)
root.right.right.right = TreeNode(4)

print(longest_path(root))  # Output: 6
