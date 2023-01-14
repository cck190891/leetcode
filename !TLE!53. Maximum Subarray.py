from typing import List
class Solution:
    """
    O(n!) TLE
    """
    def maxSubArray_1(self, nums: List[int]) -> int:
        maximum=-10^4
        for t,x in enumerate(nums):
            if x>maximum:
                maximum=x   
            while t+1<len(nums):
                t=t+1
                x=x+nums[t]
                if x>maximum:
                    maximum=x
        return maximum

    def maxSubArray(self, nums: List[int]) -> int:

if __name__=='__main__':
    sum=Solution()
    print(sum.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    

