from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_list=[x*x for x in nums]
        #can use this also
        #square_list=list(map(lambda t:t*t,nums))
        square_list.sort()
        return square_list

if __name__=='__main__':
    output=Solution()
    print(output.sortedSquares([-4,-1,0,3,10]))