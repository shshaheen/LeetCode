# Algorithm to detect cycle in a linked list using Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def detect_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # Move slow pointer by 1 step
        fast = fast.next.next     # Move fast pointer by 2 steps
        
        if slow == fast:          # Cycle detected
            return True
            
    return False                 # No cycle detected