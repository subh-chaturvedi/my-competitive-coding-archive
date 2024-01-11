# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sstep=head
        fstep=head

        for i in range(n):
            fstep=fstep.next
        
        if not fstep:
            return head.next
        
        while fstep.next:
            sstep=sstep.next
            fstep=fstep.next

        sstep.next=sstep.next.next

        return head


