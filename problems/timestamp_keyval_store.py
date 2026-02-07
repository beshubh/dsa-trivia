"""
Implement a time-based key-value data structure that supports:

    Storing multiple values for the same key at specified time stamps
    Retrieving the key's value at a specified timestamp

Implement the TimeMap class:

    TimeMap() Initializes the object.
    void set(String key, String value, int timestamp) Stores the key `key` with the value `value` at the given time timestamp.
    String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".

Note: For all calls to set, the timestamps are in strictly increasing order.
```
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"
````
"""
import collections
import unittest


ValueStruct = collections.namedtuple('ValueStruct', ['ts', 'val'])

class TimeMap:

    def __init__(self):
        self._store: dict[str, list[ValueStruct]] = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        entry = self._store[key]
        entry.append(ValueStruct(timestamp, value))
    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._store:
            return ''
        
        val_structs = self._store[key]
        value = self._bin_search(target_ts=timestamp, val_structs=val_structs)
        return value
    
    def _bin_search(self, target_ts: int, val_structs: list[ValueStruct]) -> str:
        left, right = 0, len(val_structs) - 1
        potential = '' 
        while left <= right:
            mid = left + ((right - left) // 2)
            ts_at_mid = val_structs[mid].ts
            if target_ts > ts_at_mid:
                potential = val_structs[mid].val
                left = mid + 1
            elif target_ts < ts_at_mid:
                right = mid - 1
            else:
                return val_structs[mid].val
        return potential


class TestTimeMap(unittest.TestCase):

    def setUp(self):
        self._timemap = TimeMap()
        self._timemap.set('shubh', 'nit', 0)
    

    def test_basic(self):
        self._timemap.set('shubh', 'niti', 1)
        self._timemap.set('shubh', 'nitik', 2)
        self._timemap.set('shubh', 'nitika', 3)
        self.assertEqual(self._timemap.get('shubh', 1), 'niti')
        self.assertEqual(self._timemap.get('shubh', 2), 'nitik')
        self.assertEqual(self._timemap.get('shubh', 3), 'nitika')
    
    def test_non_existing(self):
        self.assertEqual(self._timemap.get('nitika', 1), '')
    
    def test_edge(self):
        self.assertEqual(self._timemap.get('shubh', 0), 'nit')


if __name__ == '__main__':
    unittest.main()