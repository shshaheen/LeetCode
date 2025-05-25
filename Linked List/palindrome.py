# Return True if head is a palindrome, False otherwise
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(head: ListNode) -> bool:
    # Find middle using slow/fast pointer
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    # If odd length, skip middle element
    if fast:
        slow = slow.next
    # Compare reversed first half with second half
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True