from typing import List
import pprint
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        watch_point=[]
        max_len=0
        def findsame(x,y):
            same_list.append([x,y])
            watch_point.append([x,y])
            if x-1>=0 and grid[x-1][y]==grid[x][y] and [x-1,y] not in same_list:
                findsame(x-1,y)
            if x+1<len(grid) and grid[x+1][y]==grid[x][y] and [x+1,y] not in same_list:
                findsame(x+1,y)
            if y-1>=0  and grid[x][y-1]==grid[x][y] and [x,y-1] not in same_list:
                findsame(x,y-1)
            if y+1<len(grid[0]) and grid[x][y+1]==grid[x][y] and [x,y+1] not in same_list:
                findsame(x,y+1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                same_list=[]
                if grid[x][y] !=0 and [x,y]not in watch_point:
                    findsame(x,y)
                max_len=max(max_len,len(same_list))
        return(max_len)


if __name__=='__main__':
    output=Solution()
    print(output.maxAreaOfIsland(grid = [[0,0,0,0,0,0,0,0]]))