from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        second_rules=[set() for _ in range(9)]
        
        for tx,x in enumerate(board):
            
            first_rules=set()

            if tx%3==0 :
                third_rules=[set() for _ in range(3)]

            for t,y in enumerate(x):
                if y=='.':
                    continue

                if y not in first_rules :
                    first_rules.add(y)
                elif y in first_rules:
                    return False
                
                if y not in second_rules[t] :
                    second_rules[t].add(y)
                elif y in second_rules[t]:
                    return False

                if y not in third_rules[int(t/3)]:
                    third_rules[int(t/3)].add(y)
                elif y in third_rules[int(t/3)]:
                    return False 
        return True

if __name__=='__main__':
    output=Solution()
    print(output.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))