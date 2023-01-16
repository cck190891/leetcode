from typing import List
class Solution:
    def bfs(self,L):
        x,y=L
        points=[]
        if x-1 in range(self.m) : 
            if self.mat[x-1][y]== 0 and [x-1,y] not in self.view:
                return 
            else:
                points.append([x-1,y])
                self.view.append([x-1,y])

        if x+1 in range(self.m):
            if self.mat[x+1][y]== 0 and  [x+1,y] not in self.view:
                return 
            else:
                points.append([x+1,y])
                self.view.append([x+1,y])
        
        if y-1 in range(self.n) :
            if self.mat[x][y-1]== 0  and [x,y-1] not in self.view:
                return 
            else:
                points.append([x,y-1])
                self.view.append([x,y-1])

        if y+1 in range(self.n): 
            if self.mat[x][y+1]== 0  and [x,y+1 ]not in self.view:
                return  
            else:
                points.append([x,y+1])
                self.view.append([x,y+1])
        self.point_ans.append(points)
        
        for x in self.point_ans[-1]:
            self.bfs(x)
        
        

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.view=[]
        self.point_ans=[]
        self.mat=mat
        self.m=len(mat)
        self.n=len(mat[0])
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                self.point_ans=[]
                self.point_ans.append([x,y])
                if mat[x][y]==1:
                    self.bfs([x,y])
                    mat[x][y]=len(self.point_ans)
        return mat

if __name__=='__main__':
    output=Solution()
    print(output.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))