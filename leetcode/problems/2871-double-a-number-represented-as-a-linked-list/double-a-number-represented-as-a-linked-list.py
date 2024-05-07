# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        og = head

        if head:
            if head.val>4:
                og = ListNode(1,head)

        while head:
            carry=0
            if head.next:
                if head.next.val>4:
                    carry=1
            
            newval = head.val*2
            if newval>9:
                newval-=10
            
            head.val=newval+carry

            head=head.next
        
        return og