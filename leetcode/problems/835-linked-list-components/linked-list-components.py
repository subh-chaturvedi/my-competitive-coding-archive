# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans=0
        og=head

        temp=[]

        nums=set(nums)

        while head:
            if head.val in nums:
                temp.append(head.val)
                head=head.next
            else:
                if temp:
                    ans+=1
                    temp=[]
                    
                head=head.next
        
        if temp:
            ans+=1

        # print(ans)
        return ans