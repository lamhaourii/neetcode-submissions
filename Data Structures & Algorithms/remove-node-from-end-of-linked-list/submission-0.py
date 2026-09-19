# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        le=0
        current= head
        while current:
            le+=1
            current= current.next
        to_drop=le-n
        if to_drop==0:
            return head.next
        i=0
        current= head
        while current:
            if i== to_drop-1:
                current.next= current.next.next
            i+=1
            current= current.next
        return head


        