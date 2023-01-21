from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for x in range(len(prices)-1):
            if x-1>=0 and prices[x]>prices[x-1]:
                continue
                
            profit=max(max(prices[x+1:])-prices[x],profit)
        return profit
        
if __name__=='__main__':
    output=Solution()
    print(output.maxProfit([7,6,5,4,3,2]))