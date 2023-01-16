from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0
        for x in nums:
            if x >0:
                pos+=1
            elif x<0:
                neg+=1
        return max(pos,neg)

if __name__=='__main__':
    output=Solution()
    print(output.maximumCount([-2,-1,-1,1,2,3]))
    