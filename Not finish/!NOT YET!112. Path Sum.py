#Definition for a binary tree node.
# from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        while(root.left!=None or root.right!=None):
            left=path_sum(root.left,total_now)
            
    def path_sum(self,node,val):

        
        
            


# if __name__=='__main__':
#     output=Solution()
#     print(output.hasPathSum(root,22))
    