from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setList=list(set(nums))
        if len(setList) == len(nums):
            return False
        else :
            return True



if __name__=='__main__':
    sum=Solution()
    print(sum.containsDuplicate([2,2,6,7]))
    

