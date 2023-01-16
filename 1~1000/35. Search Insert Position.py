from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target) 
        else:
            nums.append(target)
            nums.sort()
            return(nums.index(target))

            
if __name__=='__main__':
    output=Solution()
    print(output.searchInsert([1,3,5,6],2))