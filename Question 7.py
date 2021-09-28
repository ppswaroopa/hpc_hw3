# Question 7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum( root, sum) -> bool:
    ans = 0
    subSum = sum - root.val

    if subSum == 0 and root.left is None and root.right is None:
        return True

    if root.left is not None:
        ans = ans or hasPathSum(root.left, subSum)
    if root.right is not None:
        ans = ans or hasPathSum(root.right, subSum)

    return ans


s = 22
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.right = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(2)

if hasPathSum(root, s):
    print("There is a root-to-leaf path with sum %d" % s)
else:
    print("There is no root-to-leaf path with sum %d" % s)

