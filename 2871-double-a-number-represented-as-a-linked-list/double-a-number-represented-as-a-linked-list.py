# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        curr = head
        while curr:
            num = num * 10 + curr.val
            curr = curr.next

        
        doubled_num = num * 2

        def reverseLinkedList(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        dummy = ListNode()
        curr = dummy
        if doubled_num == 0:
            return ListNode(0)
        while doubled_num > 0:
            digit = doubled_num % 10
            curr.next = ListNode(digit)
            curr = curr.next
            doubled_num //= 10

    
        return reverseLinkedList(dummy.next)


            