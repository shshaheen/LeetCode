# Remove nth node from end of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    # Move first n+1 steps ahead
    for _ in range(n + 1):
        if first:
            first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node from the end
    second.next = second.next.next
    
    return dummy.next