class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        forward=s[:int(len(s)/2)]
        backward=s[int(len(s)/2):]
        vowels=[]
        import re
        forward_t=len(re.findall("[aeiouAEIOU]",forward))
        backward_t=len(re.findall("[aeiouAEIOU]",backward))
        return True if forward_t==backward_t else False

if __name__=='__main__':
    output=Solution()
    print(output.halvesAreAlike("AbCd EfGh"))
    