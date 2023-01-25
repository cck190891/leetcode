from typing import List
from collections import Counter 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_c=Counter(ransomNote)
        magazine_c=Counter(magazine)
        for x in ransomNote_c:
            if ransomNote_c[x]>magazine_c[x]:
                return False
        return True
        
if __name__=='__main__':
    output=Solution()
    print(output.canConstruct("aab","baa"))