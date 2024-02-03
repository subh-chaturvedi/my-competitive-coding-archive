class LRUCache:

    def __init__(self, capacity: int):
        self.map={}
        self.cap=capacity

    def get(self, key: int) -> int:
        if key in self.map:
            ans=self.map[key]
            self.map.pop(key)
            self.map[key]=ans
            return ans
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.pop(key)
        elif len(self.map)==self.cap:
            self.map.pop(list(self.map)[0])
        self.map[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)