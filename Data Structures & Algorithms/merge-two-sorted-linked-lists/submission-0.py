# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:    
        if not list1:
            return list2
        if not list2:
            return list1
        current1= list1 
        current2= list2

        if current1.val< current2.val:
            head= current1
            list3= head
            current1= current1.next
        else:
            head= current2
            list3= head
            current2= current2.next
        while current1 or current2:
            if not current1:
                list3.next= current2
                return head
            elif not current2:
                list3.next= current1
                return head
            else:
                if current1.val< current2.val:
                   
                    list3.next=current1
                    
                    current1= current1.next
                else:
                    list3.next=current2
                    current2= current2.next
            list3= list3.next
            
            
        
    