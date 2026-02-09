from __future__ import annotations

# solution below
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        cur, prev = head, None
        print('head: ', head.val, 'tail: ', tail.val)
        while cur:
            print('prev: ', prev.val if prev else None, 'cur: ', cur.val)
            cur_next = cur.next
            cur.next = prev
            prev = cur

            if cur == tail:
                break
            cur = cur_next

        cur = prev
        while cur:
            print('revcur: ', cur.val)
            cur = cur.next
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        cur, left, count = head, head, 0
        return_head = None
        while cur:
            count += 1
            if count % k == 0:
                t = self.reverse(left, cur)
                left = cur.next
                if return_head is None:
                    return_head = t

            print('cur: ', cur.val)
            cur = cur.next
        return return_head
