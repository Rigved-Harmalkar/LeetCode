# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        new_head = self.reversed(slow.next)
        first = head
        second = new_head

        while second is not None:
            if first.val != second.val:
                self.reversed(new_head)
                return False
            first = first.next
            second = second.next

        self.reversed(new_head)
        return True


        


    
    def reversed(self,head):
        curr = head
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        