# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val=[]
        if head :
            val.append(ListNode(head.val))
            while(head.next):
                val.append(ListNode(head.next.val))
                head=head.next
                val[-1].next=val[-2] 
            return val[-1]
        else:
            print('none')
            return head

if __name__ == '__main__':
    ans=Solution()
    print(ans.reverseList([4,3,6,16,8,2]))