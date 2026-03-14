import collections


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        freq = collections.Counter(hand)
        hand.sort()
        for h in hand:
            print(freq)
            if freq[h] > 0:
                for g in range(h, h + groupSize):
                    if freq[g] == 0:
                        return False
                    freq[g] -= 1
        return True
