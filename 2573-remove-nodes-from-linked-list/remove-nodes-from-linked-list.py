# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            while stack and current.val > stack[-1].val:
                stack.pop()
            stack.append(current)
            current = current.next

        # Reconstruct the linked list from the stack
        dummy = ListNode(0)
        current = dummy
        for node in stack:
            current.next = node
            current = current.next
        current.next = None  # Set the end of the list to None

        return dummy.next

            
            