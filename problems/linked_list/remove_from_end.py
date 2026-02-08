from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def _get_size(self, head: Optional[ListNode]) -> int:
        curr, res = head, 0
        while curr:
            curr = curr.next
            res += 1
        return res

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, size = head, self._get_size(head)
        remove_at, itr = size - n, 0
        prev = None
        while itr < remove_at and curr:
            prev = curr
            curr = curr.next
            itr += 1

        if prev is None:
            curr = curr.next
            return curr

        prev.next = curr.next if curr else None
        return head
