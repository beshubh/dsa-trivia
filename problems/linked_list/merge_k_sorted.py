from __future__ import annotations

# solution below
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        minimum = float('inf')
        for cur in lists:
            if cur and cur.val < minimum:
                minimum = cur.val
                dummy.next = cur

        if dummy.next is None:
            return None
        head = dummy.next
        for cur2 in lists:
            if cur2 is dummy.next or cur2 is None:
                continue
            head = merge_lists(head, cur2)

        return head


def merge_lists(list1: ListNode, list2: ListNode):
    dummy = ListNode(0)
    tail = dummy
    cur1, cur2 = list1, list2
    while cur1 and cur2:
        if cur1.val <= cur2.val:
            tail.next = cur1
            cur1 = cur1.next
        else:
            tail.next = cur2
            cur2 = cur2.next
        tail = tail.next

    tail.next = cur1 if cur1 else cur2
    return dummy.next
