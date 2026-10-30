class Solution:
    def isValidBST(self, root):
        def validate(node, min_val, max_val):
            if node is None:
                return True

            if not (min_val < node.val < max_val):
                return False

            return (
                validate(node.left, min_val, node.val)
                and
                validate(node.right, node.val, max_val)
            )

        return validate(root, float('-inf'), float('inf'))


# Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Test Case 1
root1 = TreeNode(2, TreeNode(1), TreeNode(3))

# Test Case 2
root2 = TreeNode(5, TreeNode(1), TreeNode(4))
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

solution = Solution()

print(solution.isValidBST(root1))  # True
print(solution.isValidBST(root2))  # False