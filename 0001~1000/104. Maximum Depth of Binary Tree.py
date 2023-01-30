#BFS 修改102
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stage=0

        if root == None:
            return 0

        watch_list=[]
        watch_list.append(root)

        while watch_list:
            mem_list=[]
            for x in watch_list:
                if x.left != None:
                    mem_list.append(x.left)
                if x.right != None:
                    mem_list.append(x.right)
            stage+=1
            watch_list[:]=mem_list[:]
        return stage