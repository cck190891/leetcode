from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for x in range(1,numRows):
            mem=[]
            mem.append(1)
            for y in range(x-1):
                mem.append(ans[-1][y]+ans[-1][y+1])
            mem.append(1)
            ans.append(mem)
        return ans



if __name__=='__main__':
    output=Solution()
    print(output.generate(5))