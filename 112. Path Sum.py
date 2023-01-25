from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.path_sum(root,targetSum,0)
            
    def path_sum(self,node,target,now_sum):
        if node == None:
            return False
        now_sum+=node.val
        if node.left == None and node.right==None:
            return now_sum==target
        return (self.path_sum(node.left,target,now_sum)) or (self.path_sum(node.right,target,now_sum))

        
if __name__=='__main__':
    output=Solution()
    print(output.hasPathSum([5,4,8,11,null,13,4,7,2,null,null,null,1]))