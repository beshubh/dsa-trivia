from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head, sum_tail = None, None

        carry = 0
        while l1 and l2:
            sm = l1.val + l2.val
            cur_res = ListNode(sm % 10 + carry)
            carry = sm // 10

            if sum_head is None:
                # first element in the result list
                sum_head = cur_res
                sum_tail = cur_res
            else:
                sum_tail.next = cur_res
                sum_tail = cur_res
            l1, l2 = l1.next, l2.next

        while l1:
            sm = l1.val + carry
            cur_res = ListNode(sm % 10)
            carry = sm // 10
            sum_tail.next = cur_res
            sum_tail = cur_res
            l1 = l1.next

        while l2:
            sm = l2.val + carry
            cur_res = ListNode(sm % 10)
            carry = sm // 10
            sum_tail.next = cur_res
            sum_tail = cur_res
            l2 = l2.next

        while carry > 0:
            cur_res = ListNode(carry % 10)
            carry = carry // 10
            sum_tail.next = cur_res
            sum_tail = cur_res
        return sum_head
