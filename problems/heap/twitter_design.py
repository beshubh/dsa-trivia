import collections
import heapq


class Twitter:
    def __init__(self):
        self._tweets = collections.defaultdict(list)
        self._relationship = collections.defaultdict(set)
        self._timestamp = 0

    def get_ts(self):
        cur = self._timestamp
        self._timestamp += 1
        return cur

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (-self.get_ts(), tweetId)
        self._tweets[userId].append(tweet)

    def getNewsFeed(self, userId: int) -> list[int]:
        users_i_follow = self._relationship[userId]
        k_lists = []
        if len(self._tweets[userId]) > 0:
            k_lists.append(self._tweets[userId])
        for user in users_i_follow:
            if user != userId:
                if len(self._tweets[user]) > 0:
                    k_lists.append(self._tweets[user])

        min_heap = [(*li[-1], idx, len(li) - 1) for idx, li in enumerate(k_lists)]
        heapq.heapify(min_heap)
        result = []
        topk = 10
        while min_heap and topk > 0:
            topk -= 1
            ts, tweet, k_idx, item_idx = heapq.heappop(min_heap)
            result.append(tweet)
            item_idx -= 1
            if item_idx >= 0:
                heapq.heappush(min_heap, (*k_lists[k_idx][item_idx], k_idx, item_idx))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._relationship[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self._relationship[followerId] or followerId == followeeId:
            return
        self._relationship[followerId].remove(followeeId)
