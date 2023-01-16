from typing import List
import pprint
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        same_list=[]
        
        def findsame(x,y):
            same_list.append([x,y])
            if x-1>=0 and image[x-1][y]==image[x][y] and [x-1,y] not in same_list:
                findsame(x-1,y)
            if x+1<len(image) and image[x+1][y]==image[x][y] and [x+1,y] not in same_list:
                findsame(x+1,y)
            if y-1>=0  and image[x][y-1]==image[x][y] and [x,y-1] not in same_list:
                findsame(x,y-1)
            if y+1<len(image[0]) and image[x][y+1]==image[x][y] and [x,y+1] not in same_list:
                findsame(x,y+1)
        
        findsame(sr,sc)
        for x,y in same_list:
            image[x][y]=color
        return image

if __name__=='__main__':
    output=Solution()
    print(output.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))