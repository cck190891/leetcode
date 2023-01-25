class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        else:    
            import numpy
            mode=0
            a=0
            list=[""]*numRows
            for i in s:
                if mode == 0:
                    text=list[a]
                    list[a]=text+i   
                    a=a+1                   

                if mode ==1:
                    text=list[a]
                    list[a]=text+i  
                    a=a-1
                    
                if a == numRows-1:
                        mode=1   
                elif a == 0:
                        mode=0

            zigzag="".join(list)  
            return zigzag

if __name__=='__main__':
    output=Solution()
    print(output.convert("PAYPALISHIRING",3))
    