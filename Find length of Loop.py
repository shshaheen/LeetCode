class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #code here
        slow = head
        fast = head
        c=1
        while(fast and fast.next):
            slow=slow.next
            fast = fast.next.next
            if(slow == fast):
                while(slow.next != fast):
                    slow=slow.next
                    c+=1
                return c
        return 0