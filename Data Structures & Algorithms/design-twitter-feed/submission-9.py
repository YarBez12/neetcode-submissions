class Twitter:

    def __init__(self):
        self.usersTweets = defaultdict(list)
        self.time = 0
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.usersTweets[userId].append((tweetId, self.time))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        allFollowers = self.followers[userId]
        allFollowers.add(userId)
        for followee in self.followers[userId]:
            for post in self.usersTweets[followee][-10:]:
                postId, postTime = post
                heapq.heappush(posts, (postTime, postId))
                if len(posts) > 10:
                    heapq.heappop(posts)
        ans = []
        while posts:
            ans.append(heapq.heappop(posts)[1])
        ans.reverse()
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
