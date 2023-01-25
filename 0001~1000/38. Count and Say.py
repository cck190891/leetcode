class Solution:
    def countAndSay(self, n: int) -> str:
        
        def onecircle(text):
            final=''
            for t,x in enumerate(text):
                if t==0:
                    word=x
                    count=1
                elif x==word:
                    count+=1
                elif x!=word:
                    final+=str(count)+word
                    word=x
                    count=1
                if t+1==len(text):
                    final+=str(count)+word
                    return final

        text='1'
        for x in range(n-1):
            text=onecircle(text)
        return text
        
if __name__=='__main__':
    output=Solution()
    print(output.countAndSay(4))
    