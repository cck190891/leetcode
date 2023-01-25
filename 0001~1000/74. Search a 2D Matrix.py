from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            if target<x[0] or target>x[-1]:
                continue
            if target in x:
                return True 
            else:
                break
                
if __name__=='__main__':
    output=Solution()
    print(output.searchMatrix(matrix =[[1,3,5,7],[10,11,16,20],[23,30,34,60]],target =23))