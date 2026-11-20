from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


# Test Case 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(level_order(root1))

# Test Case 2
root2 = TreeNode(1)
print(level_order(root2))

# Test Case 3
print(level_order(None))

# Test Case 4
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(3)

print(level_order(root4))