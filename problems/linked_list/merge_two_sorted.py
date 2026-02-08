# Definition for singly-linked list.
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1, curr2 = list1, list2
        head = None
        if curr1 and curr2:
            if curr1.val < curr2.val:
                head = curr1
            else:
                head = curr2

        elif curr1:
            head = curr1
        else:
            head = curr2

        prev_smaller: ListNode | None = None
        while curr1 and curr2:
            if curr1.val < curr2.val:
                cur_smaller = curr1
                curr1_next = curr1.next
                curr1.next = curr2
                curr1 = curr1_next
            else:
                cur_smaller = curr2
                curr2_next = curr2.next
                curr2.next = curr1
                curr2 = curr2_next

            if prev_smaller:
                prev_smaller.next = cur_smaller
            prev_smaller = cur_smaller

        return head
