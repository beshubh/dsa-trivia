from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode) -> ListNode | None:
        curr = head
        prev: ListNode | None = None
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, n = head, 0
        while curr:
            curr = curr.next
            n += 1

        curr, split_at, itr = head, n // 2, 0
        split_tail: ListNode | None = None
        while itr < split_at:
            split_tail = curr
            curr = curr.next
            itr += 1

        if split_tail is None:
            return

        split_tail.next = None

        left, right = head, self.reverse(curr)

        while left and right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next if left_next else right.next

            left, right = left_next, right_next
