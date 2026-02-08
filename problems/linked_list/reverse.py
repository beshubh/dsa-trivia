# Definition for singly-linked list.
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            next_addr = cur.next
            cur.next = prev
            prev = cur
            cur = next_addr
        return prev


class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self._runner = Solution()

    def test_basic(self):
        head = ListNode(10, ListNode(5, ListNode(4, ListNode(3))))
        rev_head: ListNode = self._runner.reverseList(head)  # ty:ignore[invalid-assignment]
        self.assertEqual(rev_head.val, 3)
        self.assertEqual(rev_head.next.val, 4)


if __name__ == '__main__':
    unittest.main()
