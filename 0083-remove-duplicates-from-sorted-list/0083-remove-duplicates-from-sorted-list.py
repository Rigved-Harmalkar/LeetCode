# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not curr:
            return None
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  # Skip the duplicate
            else:
                curr = curr.next  # Move to the next node only if no duplicate is found

        return head

            
            

        