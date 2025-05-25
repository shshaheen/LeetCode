# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stA = ['A']
        stB = ['B']
        currA, currB = headA, headB
        while(currA or currB):
            if(currA):
                stA.append(currA)
                currA = currA.next
            if(currB):
                stB.append(currB)
                currB = currB.next
        prev = None
        while(stA and stB):
            nodeA = stA.pop()
            nodeB = stB.pop()
            if(nodeA != nodeB):
                return prev
            prev =nodeA
        
# Time Complexity: O(m + n) where m and n are the lengths of the two linked lists.
# Space Complexity: O(m + n) for storing the nodes in two stacks.