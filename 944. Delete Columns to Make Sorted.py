from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        zip_list=[list(row) for row in zip(*strs)]
        time=0
        for x in zip_list:
            if sorted(x) != x:
                time+=1
        return time
        
if __name__=='__main__':
    output=Solution()
    print(output.minDeletionSize(["cba","daf","ghi"]))