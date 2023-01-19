from typing import List
class Solution:

    def bfs(self,L):
        self.next_list=[]
        mem_next=[]
        for x,y in L :
            if [x,y] not in self.view and self.m>x>=0 and self.n>y>=0 :
                self.view.append([x,y])
                if x>0 and self.mat[x-1][y]==0:
                    self.mat[x][y]=1
                    return 1
                else:
                    mem_next.append([x-1,y])
                if x<self.m-1 and self.mat[x+1][y]==0:
                    self.mat[x][y]=1
                    return 1
                else:
                    mem_next.append([x+1,y])
                if y>0 and self.mat[x][y-1]==0:
                    self.mat[x][y]=1
                    return 1
                else:
                    mem_next.append([x,y-1])
                if y<self.n-1 and self.mat[x][y+1]==0:
                    self.mat[x][y]=1
                    return 1
                else:
                    mem_next.append([x,y+1])
                self.next_list=mem_next

        self.ans+=self.bfs(self.next_list)
        return self.ans+1
        

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.mat=mat
        self.ans_mat=[[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        self.m=len(mat)
        self.n=len(mat[0])
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y]==1 and self.ans_mat[x][y] == 0 :
                    self.next_list=[]
                    self.view=[]
                    self.ans=0
                    self.next_list.append([x,y])
                    final_ans=self.bfs(self.next_list)
                    self.ans_mat[x][y]=final_ans
        return self.ans_mat

if __name__=='__main__':
    output=Solution()
    print(output.updateMatrix([[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]))