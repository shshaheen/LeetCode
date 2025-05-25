#Sorting Linked List using Merge Sort algorithm
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def get_middle(head):
    if head is None or head.next is None:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
def merge_sort(head):
    if head is None or head.next is None:
        return head
    middle = get_middle(head)
    right_head = middle.next
    middle.next = None
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right_head)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    dummy = Node(0)
    current = dummy
    while left and right:
        if left.data < right.data:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    if left:
        current.next = left
    if right:
        current.next = right
    return dummy.next

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage
if __name__ == "__main__":
    arr = [4, 2, 1, 3]
    head = create_linked_list(arr)
    print("Original Linked List:")
    print_linked_list(head)
    
    sorted_head = merge_sort(head)
    print("Sorted Linked List:")
    print_linked_list(sorted_head)