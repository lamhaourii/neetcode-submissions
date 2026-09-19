# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        previous=None
        current=head
        next=head.next
        while current.next:
            next=current.next 
            current.next= previous
            previous= current
            current= next

            
        current.next= previous
        return current

            

            

        

        

        
        
        


        