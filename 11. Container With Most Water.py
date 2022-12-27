class Solution:
    def maxArea(self, height) -> int:
        maxValue=0
        left=0
        right=len(height)-1
        while left<right:
            maxValue=max(maxValue,((right-left)*min(height[left],height[right])))
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return maxValue
#左右指針 向內收縮
if __name__=='__main__':
    output=Solution()
    print(output.maxArea([1,8,6,2,5,4,8,3,7]))