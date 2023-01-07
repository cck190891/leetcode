from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        l_list=nums[:-k]
        r_list=nums[-k:]
        nums[:]=r_list+l_list

if __name__=='__main__':
    output=Solution()
    print(output.rotate([1,2],3))