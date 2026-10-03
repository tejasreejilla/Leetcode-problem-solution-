import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.time = 0

        # user -> set of users they follow
        self.following = defaultdict(set)

        # user -> list of (time, tweetId)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        # User sees their own tweets
        users = self.following[userId] | {userId}

        for user in users:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(heap, (time, tweetId))

                # Keep only the 10 most recent tweets
                if len(heap) > 10:
                    heapq.heappop(heap)

        # Heap contains the 10 newest.
        # Return newest -> oldest.
        return [tweetId for time, tweetId in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)