from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=0
        ans=[None for x in range(len(temperatures))]
        for t,x in enumerate(temperatures):
            a=1
            while (t+a)<=len(temperatures)-1 and temperatures[t]>=temperatures[t+a] :
                a+=1
            if t+a == len(temperatures):
                a=0
            ans[t]=a

        return ans

if __name__=='__main__':
    output=Solution()
    print(output.dailyTemperatures([73,74,75,71,69,72,76,73]))
    