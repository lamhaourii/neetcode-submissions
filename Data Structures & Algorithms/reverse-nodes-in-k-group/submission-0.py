# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        le= 0
        current= head
        while current:
            le+= 1
            current= current.next
        grps= le//k
        head_= head
        current= head
        last= None
        while grps:
            i=1
            first= current
            prev=None
            while current:
                next=current.next
                current.next=prev
                prev= current
                current= next
                if i==k:
                    
                    if grps==le//k:
                        head_=prev
                    grps-=1
                    break
                i+=1
            if last:
                last.next= prev
            first.next=current
            last=first
        return head_
            
            
            


        
        