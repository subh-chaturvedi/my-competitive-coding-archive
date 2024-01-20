# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        arr=[]

        for head in lists:
            tempNode=head
            while tempNode:
                arr.append(tempNode.val)
                tempNode=tempNode.next
        
        if not arr:
            return None

        arr.sort()

        LL=ListNode(arr[0])

        tempNode=LL

        for _ in arr[1:]:
            tempNode.next=ListNode(_)
            tempNode=tempNode.next
        
        return LL



        