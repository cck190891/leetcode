"""
遞迴會O(n*n)
用dictionary紀錄次方出現次數 
如果平方有在裡面代表出現過 
將其次數加入+1放到自己位置

如果內層使用while可以過

另解先產生全部dict之後尋找平方後
"""
# class Solution:
#     def longestSquareStreak(self, nums) -> int:
#         nums=list(set(nums))
#         nums.sort(reverse=True)
#         table={}
#         for x in nums:
#             if x*x in table:
#                 table[x]=table[x*x]+1
#             else:
#                 table[x]=1

#         if max(table.values())>1:
#             return max(table.values())
#         else :
#             return -1

from math import isqrt
class Solution:
    def longestSquareStreak(self, nums) -> int:
        dp = dict(zip(nums, [1]*len(nums)))
        for x in sorted(nums): 
            v = isqrt(x)

            if v**2 == x and v in dp: dp[x] = 1 + dp[v]
        ans = max(dp.values())
        return ans if ans > 1 else -1

if __name__ == '__main__':
    ans=Solution()
    print(ans.longestSquareStreak([4,3,6,16,8,2]))