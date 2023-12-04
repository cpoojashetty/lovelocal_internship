class TreeNode:
    def __init__(self, val=0, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r

def lowestAncestor(root, p, q):
    if not root:
        return None

    # If both nodes are smaller than the root, LCA is in the left subtree
    if p.val < root.val and q.val < root.val:
        return lowestAncestor(root.left, p, q)

    # If both nodes are larger than the root, LCA is in the right subtree
    elif p.val > root.val and q.val > root.val:
        return lowestAncestor(root.right, p, q)

    # If one node is on the left and the other is on the right, the current root is the LCA
    else:
        return root

# Test cases
# Example 1
root1 = TreeNode(6)
root1.l = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
root1.r = TreeNode(8, TreeNode(7), TreeNode(9))
p1 = TreeNode(2)
q1 = TreeNode(8)
print(lowestAncestor(root1, p1, q1).val)  # Output: 6

# Example 2
root2 = TreeNode(6)
root2.l = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
root2.r = TreeNode(8, TreeNode(7), TreeNode(9))
p2 = TreeNode(2)
q2 = TreeNode(4)
print(lowestAncestor(root2, p2, q2).val)  # Output: 2

# Example 3
root3 = TreeNode(2, TreeNode(1))
p3 = TreeNode(2)
q3 = TreeNode(1)
print(lowestAncestor(root3, p3, q3).val)  # Output: 2
