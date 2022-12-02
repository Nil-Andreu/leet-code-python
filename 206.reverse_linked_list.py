from typing import Optional
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]  (this in a LL)
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]  (this in a LL)
Output: [2,1]

Example 3:
Input: head = []  (this in a LL)
Output: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        One solution would be to first go through all the list, and save the values.
        And then go through the list another time, changing the values in a saved list reversed.

        But we could solve this going through the list only once.
        As we go through the list, we keep track of which is the current node, previous node and the next one.
        So when we are in a position, we can save which is the next (curr.next). Then this curr.next = previous node. And finally we update the positions: prev = current node, curr = next (one pass forward), and in the next loop the next would be updated to be the curr.next.
        """

        curr = head
        prev = next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev