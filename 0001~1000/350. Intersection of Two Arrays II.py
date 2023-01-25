from typing import List
#可以改成雙指針同時查看

#直接回圈並檢查
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        
        if len(nums1) > len(nums2):
            for x in nums2:
                if x in nums1:
                    nums1.remove(x)
                    ans.append(x)
        else:
            for x in nums1:
                if x in nums2:
                    nums2.remove(x)
                    ans.append(x)
        return ans

if __name__=='__main__':
    output=Solution()
    print(output.intersect([1,2,2,1],[2,2]))