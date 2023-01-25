from typing import List
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        good=1
        bad=n

        if isBadVersion(good):
            return good
        
        while(True):
            if(isBadVersion(int((good+bad)/2)) == False):
                good=int((good+bad)/2)
            else:
                bad=int((good+bad)/2)

            if bad==good+1:
                break
        return(bad)

#題目targer
def isBadVersion(x):
    if x > 0 :
        return True   
    else:
        return False

if __name__=='__main__':
    output=Solution()
    print(output.firstBadVersion(2))