from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0])!=r*c:
            return mat
        mem_list=[]
        ans_list=[]
        for x in mat:
            for y in x:
                mem_list.append(y)
                if len(mem_list)==c:
                    ans_list.append(mem_list)
                    mem_list=[]

        return ans_list

if __name__=='__main__':
    output=Solution()
    print(output.matrixReshape())