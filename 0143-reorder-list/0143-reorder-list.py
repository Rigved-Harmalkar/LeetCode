# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        # To find the two halves
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Second Half
        second = slow.next

        # End of the first Half
        slow.next = None

        first = head
        second = self.reverse(second)

        while second:
            tmp1, tmp2 = first.next,second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


    # To reverse the second half of the linked List
    def reverse(self,head):
        curr = head
        prev = None
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node

        return prev
        