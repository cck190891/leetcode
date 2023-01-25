#雙指針

class Solution(object):
    def twoSum(self, nums, target):
        sort_num=sorted(nums)
        l_p=0
        r_p=len(nums)-1
        while l_p<r_p:
            if sort_num[l_p]+sort_num[r_p]==target:
                if sort_num[l_p]==sort_num[r_p]:
                    return [nums.index(sort_num[l_p]),nums.index(sort_num[r_p],nums.index(sort_num[l_p])+1)]
                else :
                    return [nums.index(sort_num[l_p]),nums.index(sort_num[r_p])]
            elif sort_num[l_p]+sort_num[r_p]>target:
                r_p-=1
            elif sort_num[l_p]+sort_num[r_p]<target:
                l_p+=1
        return 'no answer'

#暴力法
class Solution_(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    ans=Solution()
    print(ans.twoSum([3,3],6))