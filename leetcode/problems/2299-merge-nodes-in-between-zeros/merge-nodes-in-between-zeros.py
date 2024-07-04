# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        og=head

        sumd=0
        start=head
        head=head.next

        while head:
            if head.val==0:
                head.val=sumd
                sumd=0
                start.next=head
                start=head
                
                head=head.next
            else:
                sumd+=head.val
                head=head.next
        
        return og.next