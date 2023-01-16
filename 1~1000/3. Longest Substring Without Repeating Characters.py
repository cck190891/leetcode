class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        alllist=[]
        strlist=''
        for x in s:
            if x not in strlist:
                strlist+=x
                alllist.append(strlist)

            else:
                alllist.append(strlist)
                strlist+=x
                print(strlist)
                listx=list(strlist) 
                listx=listx[listx.index(x)+1:]
                strlist=''.join(listx)
                print(listx)
                alllist.append(strlist)

        print(alllist)
        try:
            total=len(max(alllist,key=len)) 
        except:
            total=0

        return total 

if __name__=='__main__':
    output=Solution()
    print(output.lengthOfLongestSubstring(''))
    