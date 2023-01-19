# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mem=[]
        
        while list1:
            mem.append(list1.val)
            list1=list1.next
        while list2:
            mem.append(list2.val)
            list2=list2.next

        mem.sort()
        if not mem:
            return list1
        elif len(mem)==1:
            return ListNode(mem[-1])
            
        node_mem=ListNode(mem[-1])
        for t in range(len(mem)-1):    
            ans=ListNode(mem[len(mem)-2-t])
            ans.next=node_mem
            node_mem=ans
        return ans