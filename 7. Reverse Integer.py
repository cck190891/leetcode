class Solution:
    def reverse(self, x: int) -> int:

        list=[]
        negative=''
        for a in str(x):
            if a != '-':
                list.append(a)
            else:
                negative="-"
        list.reverse()
        reverse_int=int(negative+"".join(list))
        if reverse_int > 2**31 or reverse_int < -2**31:
            return 0

        return reverse_int


if __name__=='__main__':
    output=Solution()
    print(output.reverse(123))
    