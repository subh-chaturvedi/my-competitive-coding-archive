# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return False

        fstep =head
        sstep = head

        while sstep and fstep:
            sstep=sstep.next
            fstep=fstep.next
            if not fstep:
                return False
            fstep=fstep.next

            if sstep==fstep:
                return True
        
        return False
