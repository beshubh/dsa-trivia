from __future__ import annotations

import unittest
import threading
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    key: Any
    val: Any
    prev: Node | None = None
    next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self._head = Node('__head', '__head')
        self._tail = Node('__tail', '__tail')
        self._head.next, self._tail.prev = self._tail, self._head

    def append(self, node: Node) -> None:
        current_tail_prev = self._tail.prev
        if current_tail_prev is None:
            raise ValueError('impossible')

        current_tail_prev.next = node
        node.prev = current_tail_prev
        self._tail.prev = node
        node.next = self._tail

    def remove(self, ref: Node) -> None:
        if ref is None:
            raise ValueError('`ref` cannot be None')
        if ref is self._head:
            raise ValueError('cannot delete the head node')
        if ref is self._tail:
            raise ValueError('cannot delete the tail node')
        prev = ref.prev
        next = ref.next
        prev.next = next  # type: ignore
        next.prev = prev  # type: ignore

    def remove_head(self) -> Node:
        node = self._head.next
        self.remove(node)
        return node  # type: ignore


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._size = 0
        self._ll = LinkedList()
        self._store: dict[Any, Node] = dict()
        self._lock = threading.Lock()

    def put(self, key: Any, val: Any) -> None:
        with self._lock:
            if key in self._store:
                node = self._store[key]
                self._ll.remove(node)
                node.val = val
                self._ll.append(node)
                self._store[key] = node
            else:
                node = Node(key=key, val=val)
                self._store[key] = node
                self._ll.append(node)
                self._size += 1
            while self._size > self._capacity:
                node = self._ll.remove_head()
                del self._store[node.key]
                self._size -= 1

    def get(self, key: Any) -> Any | None:
        with self._lock:
            if key not in self._store:
                return None
            node = self._store[key]
            self._ll.remove(node)
            self._ll.append(node)
            return node.val


class TestLRUCache(unittest.TestCase):
    def assert_cache_integrity(self, cache: LRUCache):
        self.assertEqual(cache._size, len(cache._store))

        count = 0
        seen_keys = set()
        node = cache._ll._head.next
        while node is not cache._ll._tail:
            self.assertIsNotNone(node)
            self.assertIsNotNone(node.prev)
            self.assertIsNotNone(node.next)
            self.assertIs(cache._store[node.key], node)
            self.assertNotIn(node.key, seen_keys)
            seen_keys.add(node.key)
            count += 1
            node = node.next

        self.assertEqual(count, cache._size)
        self.assertEqual(seen_keys, set(cache._store))

    def test_get_missing_key_returns_none(self):
        cache = LRUCache(2)
        self.assertIsNone(cache.get("missing"))

    def test_put_and_get_single_item(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        self.assertEqual(cache.get("a"), 1)

    def test_put_multiple_items_within_capacity(self):
        cache = LRUCache(3)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("b"), 2)
        self.assertEqual(cache.get("c"), 3)

    def test_evicts_least_recently_used_item(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get("b"), 2)
        self.assertEqual(cache.get("c"), 3)

    def test_get_marks_item_as_recently_used(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        self.assertEqual(cache.get("a"), 1)
        cache.put("c", 3)
        self.assertEqual(cache.get("a"), 1)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("c"), 3)

    def test_updating_existing_key_changes_value(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("a", 10)
        self.assertEqual(cache.get("a"), 10)

    def test_updating_existing_key_marks_it_recently_used(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("a", 10)
        cache.put("c", 3)
        self.assertEqual(cache.get("a"), 10)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("c"), 3)

    def test_capacity_one_keeps_only_most_recent_item(self):
        cache = LRUCache(1)
        cache.put("a", 1)
        self.assertEqual(cache.get("a"), 1)
        cache.put("b", 2)
        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get("b"), 2)

    def test_repeated_gets_do_not_change_returned_value(self):
        cache = LRUCache(2)
        cache.put("x", 100)
        self.assertEqual(cache.get("x"), 100)
        self.assertEqual(cache.get("x"), 100)
        self.assertEqual(cache.get("x"), 100)

    def test_supports_different_key_and_value_types(self):
        cache = LRUCache(3)
        cache.put(1, "one")
        cache.put((2, 3), {"v": 23})
        cache.put("three", [3])
        self.assertEqual(cache.get(1), "one")
        self.assertEqual(cache.get((2, 3)), {"v": 23})
        self.assertEqual(cache.get("three"), [3])

    def test_eviction_order_after_mixed_gets_and_puts(self):
        cache = LRUCache(3)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("b"), 2)
        cache.put("d", 4)
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("b"), 2)
        self.assertIsNone(cache.get("c"))
        self.assertEqual(cache.get("d"), 4)

    def test_concurrent_puts_preserve_capacity_and_internal_state(self):
        cache = LRUCache(5)
        start = threading.Barrier(6)
        errors = []

        def worker(worker_id: int):
            try:
                start.wait()
                for value in range(50):
                    cache.put(f"{worker_id}-{value}", value)
            except BaseException as exc:
                errors.append(exc)

        threads = [
            threading.Thread(target=worker, args=(worker_id,))
            for worker_id in range(5)
        ]

        for thread in threads:
            thread.start()
        start.wait()
        for thread in threads:
            thread.join()

        self.assertEqual(errors, [])
        self.assertLessEqual(cache._size, cache._capacity)
        self.assertLessEqual(len(cache._store), cache._capacity)
        self.assert_cache_integrity(cache)

    def test_concurrent_reads_and_writes_keep_cache_consistent(self):
        cache = LRUCache(3)
        cache.put("shared", 0)
        cache.put("warm-1", 1)
        cache.put("warm-2", 2)

        start = threading.Barrier(5)
        errors = []

        def writer(worker_id: int):
            try:
                start.wait()
                for value in range(100):
                    cache.put("shared", (worker_id, value))
                    cache.put(f"worker-{worker_id}", value)
            except BaseException as exc:
                errors.append(exc)

        def reader():
            try:
                start.wait()
                for _ in range(200):
                    value = cache.get("shared")
                    self.assertTrue(value is None or isinstance(value, tuple))
                    cache.get("warm-1")
                    cache.get("worker-0")
                    cache.get("worker-1")
            except BaseException as exc:
                errors.append(exc)

        threads = [
            threading.Thread(target=writer, args=(0,)),
            threading.Thread(target=writer, args=(1,)),
            threading.Thread(target=reader),
            threading.Thread(target=reader),
        ]

        for thread in threads:
            thread.start()
        start.wait()
        for thread in threads:
            thread.join()

        self.assertEqual(errors, [])
        self.assertLessEqual(cache._size, cache._capacity)
        self.assertLessEqual(len(cache._store), cache._capacity)
        self.assert_cache_integrity(cache)
        shared_value = cache.get("shared")
        self.assertTrue(shared_value is None or isinstance(shared_value, tuple))


if __name__ == '__main__':
    unittest.main()
