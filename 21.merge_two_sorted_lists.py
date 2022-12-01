from typing import Optional

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        We can iterate through the lists, and in each position of the, set the next of the current list to that list.
        """
        
        cur = head = ListNode()

        while list1 and list2:
            # Check which values in that list are higher
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next

            else:
                cur.next = list1
                list1 = list1.next
            
            # Move one position up
            cur = cur.next
        
        # In the case there is still some part of the lists we have not visited
        if list1 or list2:
            cur.next = list1 if list1 else list2
        
        return head.next