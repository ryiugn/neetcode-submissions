class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) #userId = list[[count, tweetId]]
        self.followeeMap = defaultdict(set) #userId = set(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followeeMap[userId]
        followees.add(userId)
        heap = []
        for followee in followees:
            if len(self.tweetMap[followee]) > 0:
                lastIndex = len(self.tweetMap[followee]) - 1
                count, tweetId = self.tweetMap[followee][lastIndex]
                heap.append([count, tweetId, followee, lastIndex - 1])
        heapq.heapify(heap)
        res = []
        while heap and len(res) < 10:
            count, tweetId, followee, nextIndex = heapq.heappop(heap)
            res.append(tweetId)
            if nextIndex >= 0:
                count, tweetId = self.tweetMap[followee][nextIndex]
                heapq.heappush(heap, [count, tweetId, followee, nextIndex - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)
