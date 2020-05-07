# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self,root,n):
        if root is None:
            return 0
        if root.val == n:
            return 0
        
        return 1 + self.depth(root.left,n) + self.depth(root.right,n)  
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = [root]
        res = False
        while(len(q)):
            c = len(q)
            mydict = {}
            while(c):
                c -= 1
                temp = q.pop(0)
                if temp.left:
                    q.append(temp.left)
                    if temp.left.val == x:
                        mydict[x] = temp.val
                    if temp.left.val == y:
                        mydict[y] = temp.val
                if temp.right:
                    q.append(temp.right)
                    if temp.right.val == x:
                        mydict[x] = temp.val
                    if temp.right.val == y:
                        mydict[y] = temp.val
                        
            if len(mydict) == 2:
                if mydict[x] != mydict[y]:
                    return True
        return False
                
                
                
        
        