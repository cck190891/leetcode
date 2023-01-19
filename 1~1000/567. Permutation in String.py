import time
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_list=list(s1)
        s2_list=list(s2)
        check=[]
        
        for t,x in enumerate(s2_list):
            if x in s1_list:
                s1_list.remove(x)
                check.append(x)
                if not s1_list:
                    return True
            else:
                if bool(check) and x == check[0]:
                    check.remove(x)
                    check.append(x)
                else:
                    if bool(check) and x in check:
                        s1_list=s1_list+check[:check.index(x)]
                        check=check[check.index(x)+1:]+[x]
                    else:
                        s1_list=list(s1)
                        check=[]

        return False

if __name__=='__main__':
    output=Solution()
    print(output.checkInclusion("abcd"\
        ,"abdbac"))