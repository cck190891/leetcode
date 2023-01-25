from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not m :
            nums1[:]=nums2
        elif m and n:
            nums1[:]=nums1[:m]+nums2[:n]
            nums1.sort()
            
        print(nums1)
if __name__=='__main__':
    output=Solution()
    print(output.merge(nums1 =[1,2,3,0,0,0],m =3,nums2 =[2,5,6],n=3))