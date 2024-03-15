class Twitter:
    import heapq

    def __init__(self):
        self.feed = []
        self.followMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followMap:
            self.followMap[userId] = [userId]
        
        self.feed.append([tweetId,userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        
        fed=0
        ans=[]

        if userId in self.followMap:
            self.followMap[userId].append(userId)

        for i in self.feed[::-1]:
            if i[1] in self.followMap[userId]:
                ans.append(i[0])
                fed+=1
                if fed>=10:
                    break
        
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].append(followeeId)
        else:
            self.followMap[followerId] = [followerId,followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)
            
            


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)