import heapq


class Twitter:
    def __init__(self):
        self.cnt = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.cnt, tweetId))
        self.cnt += 1
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        for uid in self.following.get(userId, set()) | {userId}:
            if uid in self.tweets and self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-t, tid, uid, idx))

        res = []
        while heap and len(res) < 10:
            _, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)
            if idx > 0:
                t, tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-t, tid, uid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


"""
time:
- postTweet, follow, unfollow: O(1).
- getNewsFeed: O(f log f) where f = number of followees.
- merges f tweet lists via heap, pop at most 10 times.

space: O(U) where U = number of users
- each user stores at most 10 tweets.
- getNewsFeed heap holds at most f entries.

"""
