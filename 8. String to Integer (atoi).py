class Solution:
    def myAtoi(self, s: str) -> int:
        import re
        s=s.strip()
        num=re.findall("[+-]?[0-9|.]+",s)
        word=re.findall("(.*?)[+-]?[0-9|.]+",s)
        print(num)
        print(word)

        if len(num)==0:
            return 0
        else :
            if word != None:
                if len(word[0])!=0:
                    return 0
            final=num[0]
            if '.' in final:
                final = float(final)
            else:
                final = int(final)

            if final >=2**31-1:
                final =2**31-1
            elif  final<=-2**31:
                final=-2**31
            
            return int(final)
                
if __name__=='__main__':
    output=Solution()
    print(output.myAtoi("-987 words and"))
    