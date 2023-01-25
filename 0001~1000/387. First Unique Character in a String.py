from typing import List
from collections import Counter 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        total=Counter(s)
        
        for t,x in enumerate(s):
            if total[x] == 1:
                return t
        return -1

if __name__=='__main__':
    output=Solution()
    print(output.firstUniqChar("leetcode"))