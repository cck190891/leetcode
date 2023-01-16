from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=float('inf')
        for f in range(len(nums)-1):
            l,r=f+1,len(nums)-1
            while l<r:
                if abs(nums[f]+nums[l]+nums[r]-target) < abs(ans-target):
                    ans=nums[f]+nums[l]+nums[r]
                    print(nums[f],nums[l],nums[r],ans,abs(nums[f]+nums[l]+nums[r]-target))
                if nums[f]+nums[l]+nums[r]<target:
                    l+=1
                elif nums[f]+nums[l]+nums[r]>target:
                    r-=1
                else:
                    return nums[f]+nums[l]+nums[r]

        return ans

if __name__=='__main__':
    sum=Solution()
    print(sum.threeSumClosest([-1,2,1,-4],1))
    
    
