# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        size = len(preorder)
        q = []
        q.append(root)
        i = 1
        
        while i < size:
            temp = None
            
            while(len(q) and preorder[i] > q[-1].val):
                temp = q.pop()
                
            if temp!= None:
                temp.right = TreeNode(preorder[i])
                q.append(temp.right)
            else:
                temp = q[-1]
                temp.left = TreeNode(preorder[i])
                q.append(temp.left)
            i += 1
        return root
                
        