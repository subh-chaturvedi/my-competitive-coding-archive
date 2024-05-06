# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stck = []
        # stck.append(head)

        newhead=head

        while head:
            
            while stck and stck[-1].val<head.val:
                stck.pop(-1)
                
            if len(stck)==0:
                newhead=head
                stck.append(head)
            else:
                stck[-1].next=head
                stck.append(head)
            
            head=head.next
        
        return newhead
        