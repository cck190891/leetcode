from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        L1=[]
        L2=[]

        m,n=len(grid),len(grid[0])
        check=tuple([0,1,0,-1,0])
        count=0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    L1.append([x,y])
                elif grid[x][y] == 1:
                    L2.append([x,y])

        if not L1 and L2:
            return -1
        if not L2:
            return 0

        while(L1):
            L2=L1
            L1=[]
            count+=1
            for one in L2:
                x,y=one
                for t in range(4):
                    if m>x+check[t]>=0 and n>y+check[t+1]>=0 and grid[x+check[t]][y+check[t+1]]==1:
                        grid[x+check[t]][y+check[t+1]]=2
                        L1.append([x+check[t],y+check[t+1]])

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    return -1
        return count-1
if __name__ == '__main__':
    ans=Solution()
    print(ans.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))