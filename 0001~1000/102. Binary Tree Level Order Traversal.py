# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[[] for x in range(2000)]
        stage=0

        if root == None:
            return []

        watch_list=[]
        watch_list.append(root)

        while watch_list:
            mem_list=[]
            for x in watch_list:
                ans[stage].append(x.val)
                if x.left != None:
                    mem_list.append(x.left)
                if x.right != None:
                    mem_list.append(x.right)
            stage+=1
            watch_list[:]=mem_list[:]
        ans =[x for x in ans if x != []]
        return ans