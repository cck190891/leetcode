from typing import List
class Solution:


    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mask=[[0 for _ in len(mat[0])] for _ in len(mat)]
        same_list=[]
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                mask[x][y]=self.search(mat,x,y,same_list)
        return mask

if __name__=='__main__':
    output=Solution()
    print(output.updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]]))