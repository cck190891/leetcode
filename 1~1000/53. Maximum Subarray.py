from typing import List

'''
累加 
檢查需不需要前面的值，
如果跟前值相加大於自己，代表前值有用，

time O(n)
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> bool:
        ans_list=[-float('Inf')]
        for x in nums:
            ans_list.append(max(ans_list[-1]+x,x))
        return(max(ans_list))



'''
暴力法
time O(n*n!)
'''
class Solution_:
    def maxSubArray_(self, nums: List[int]) -> int:
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

if __name__=='__main__':
    ans=Solution()
    print(ans.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    
