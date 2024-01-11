# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1=headA
        t2=headB
        st=set()

        while t1:
            st.add(t1)
            t1=t1.next
        
        while t2:
            if t2 in st:
                return t2
            else:
                t2=t2.next
        
        return None