# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#listnode 先轉list處理 之後再轉回listnode
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        while True:
            list1.append(l1.val)
            l1=l1.next
            if l1 ==None:
                break
        while True:
            list2.append(l2.val)
            l2=l2.next
            if l2 ==None:
                break

        l1r=map(str,list1[::-1])
        l2r=map(str,list2[::-1])

        l1ri=int(''.join(l1r))
        l2ri=int(''.join(l2r))

        total=l1ri+l2ri
        total=list(str(total))
        total=total[::-1]

        listnode_str=",".join(total)
        return ListNode(listnode_str)

        
if __name__=='__main__':
    sum=Solution()
    print(sum.addTwoNumbers([2,4,3],[5,6,4]))
    

