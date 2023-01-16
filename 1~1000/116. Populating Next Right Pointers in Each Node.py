from typing import Optional
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
'''
預設是None 要把root的next補上  
所以只需要補上兩點中間
1)
左邊指到右邊
2)
右邊指到下一個點的左邊 
就能補齊中間
'''
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
if __name__=='__main__':
    output=Solution()
    print(output.connect())