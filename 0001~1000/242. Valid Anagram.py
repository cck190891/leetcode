from typing import List
from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ransomNote_c=Counter(s)
        magazine_c=Counter(t)
        if ransomNote_c==magazine_c:
            return True
        
if __name__=='__main__':
    output=Solution()
    print(output.isAnagram("aab","baa"))