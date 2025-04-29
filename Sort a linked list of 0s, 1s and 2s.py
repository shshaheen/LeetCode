	
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
class Solution:
    def segregate(self, head):
        #code here
        zerolist = Node(-1)
        onelist = Node(-1)
        twolist= Node(-1)
        curr = head
        
        zeros = zerolist
        ones = onelist
        twos = twolist
        while(curr):
            if(curr.data == 0):
                zeros.next = curr
                zeros = zeros.next
            elif(curr.data == 1):
                ones.next = curr 
                ones = ones.next
            else:
                twos.next = curr
                twos = twos.next
            curr = curr.next
        zeros.next = onelist.next if onelist.next else twolist.next
        ones.next= twolist.next
        twos.next=None
        head = zerolist.next
        return head
        