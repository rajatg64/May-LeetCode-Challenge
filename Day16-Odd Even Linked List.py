# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        head1 = head
        odd = ListNode(0)
        even = ListNode(0)
        oddhead = odd
        evenhead = even
        
        flip = False
        while(head):
            if flip == False:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
                
            head = head.next
            flip = not flip
            
        even.next = None
        odd.next = evenhead.next   
        return oddhead.next
        
              
                
            
        