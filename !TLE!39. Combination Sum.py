from typing import List
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(candidates,target,'')


    def dfs(self,candidates,target,view):
        for x in candidates:
            print(target,view,x)

            if target-x>0:
                print('target>x')
                view+=str(x)
                self.dfs(candidates,target-x,view)
                

            elif target-x<0:
                view-=str(x)
                print('target<x')
                return

if __name__=='__main__':
    sum=Solution()
    print(sum.combinationSum([2,3,6,7],7))
    

