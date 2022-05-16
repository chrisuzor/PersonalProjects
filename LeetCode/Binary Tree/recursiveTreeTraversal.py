class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def maximunDepth(root):
    if root is None:
        return 0

    leftDepth = maximunDepth(root.left)
    rightDepth = maximunDepth(root.right)

    return max(leftDepth, rightDepth) + 1


def topToBottom(root, depth=1, answer=0):
    if root is None:
        return answer

    if root.left is None and root.right is None:
        answer = max(answer, depth)

    topToBottom(root.left, depth + 1)
    topToBottom(root.right, depth + 1)

    return answer


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.right.left.right = Node(7)


# print("The max depth is:", maximunDepth(root))
print("The max depth is:", topToBottom(root))
