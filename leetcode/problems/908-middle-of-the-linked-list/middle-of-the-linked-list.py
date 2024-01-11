# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sstep=head
        lstep=head

        
        while sstep is not None:
            lstep=lstep.next
            if lstep is None:
                return sstep
            lstep=lstep.next
            if lstep is None:
                return sstep.next
            sstep=sstep.next
