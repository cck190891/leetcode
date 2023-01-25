from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        target_point=0
        neg_point=target_point+1
        pos_point=len(nums)-1
        if nums[0]>0 or nums[-1]<0 or len(nums)<3:
            return []
        for _ in range(len(nums)-2):
            if nums[pos_point-1]+nums[pos_point]+nums[target_point]>=0 :
                while neg_point<pos_point:
                    if nums[neg_point]+nums[pos_point]+nums[target_point]==0:
                        if [nums[target_point],nums[neg_point],nums[pos_point]] not in ans:
                            ans.append([nums[target_point],nums[neg_point],nums[pos_point]])
                        while neg_point<pos_point  and nums[neg_point]==nums[neg_point+1] :
                            neg_point+=1
                        while neg_point<pos_point  and nums[pos_point]==nums[pos_point-1]   :
                            pos_point-=1  

                        neg_point+=1
                        pos_point-=1

                    elif nums[neg_point]+nums[pos_point]+nums[target_point]<0:
                        neg_point+=1
                    elif nums[neg_point]+nums[pos_point]+nums[target_point]>0:
                        pos_point-=1

            target_point+=1
            neg_point=target_point+1
            pos_point=len(nums)-1     
        return ans
if __name__=='__main__':
    sum=Solution()
    print(sum.threeSum([0,0,0]))


