# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=None
        curr=head
        if not curr:
            return None
        front=curr.next
        if not front:
            return head

        while front:
            
            curr.next=prev
            prev=curr
            curr=front
            front=front.next
            if not front:
                curr.next=prev
                prev=curr
        
        return prev
