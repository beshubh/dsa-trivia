from __future__ import annotations


from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None
        while slow and fast:
            if slow is fast:
                return True

            slow = slow.next
            fast = fast.next.next if fast.next else None
        return False
