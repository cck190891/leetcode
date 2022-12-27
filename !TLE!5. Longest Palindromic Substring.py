class Solution:
    def longestPalindrome(self, s: str) -> str:
        #time limit exceeded 
        strlist=list(s)

        for x in range(len(s),0,-1):
            for y in range(len(s)-x+1):
                alist=strlist[y:y+x] 
                revers_alist=alist[::-1]
                if alist==revers_alist:
                    return ''.join(alist)



if __name__=='__main__':
    output=Solution1()
    print(output.longestPalindrome("aba"))
    