class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() or word.isupper() or word.istitle():
            return True
        return False

if __name__=='__main__':
    output=Solution()
    print(output.detectCapitalUse("abba"))