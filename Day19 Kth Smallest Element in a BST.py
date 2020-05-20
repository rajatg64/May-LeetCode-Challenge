class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        lst = []
        def inOrder(root):
            if root is None:
                return
            inOrder(root.left)
            lst.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return lst[k-1]
            
        