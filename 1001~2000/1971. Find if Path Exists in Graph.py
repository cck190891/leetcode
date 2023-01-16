from typing import List
"""注意結束條件 跟 已檢查過的點"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        origin=[[] for x in range(n)]
        for e0,e1 in edges:
            origin[e0].append(e1)
            origin[e1].append(e0)
        visit=[]

        def dfs(des):
            if des == source:
                return True
            if des not in visit:
                visit.append(des)
                for x in origin[des]:
                    if dfs(x):
                        return True
            return False
        return dfs(destination)
            

if __name__ == '__main__':
    ans=Solution()
    print(ans.validPath(n =3,edges =[[0,1],[1,2],[2,0]],source =0,destination =2))