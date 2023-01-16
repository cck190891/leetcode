class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list=s.split(' ')
        pattern_list=list(pattern)
        if len(word_list) != len(pattern_list):
            return 0
        zip_list=set(zip(word_list,pattern_list))
        word_check,pattern_check=list(zip(*zip_list))
        if len(pattern_check) == len(set(pattern_check)):
            if len(word_check) != len(set(word_check)):
                return False
            return True
        else:
            return False

if __name__=='__main__':
    output=Solution()
    print(output.wordPattern("abba","dog cat cat dog"))