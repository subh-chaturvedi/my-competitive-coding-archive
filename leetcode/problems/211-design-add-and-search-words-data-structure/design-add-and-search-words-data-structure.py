class trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = trie()

    def addWord(self, word: str) -> None:

        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c]=trie()
            curr = curr.children[c]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(root,word):
            curr = root

            for c in range(len(word)):
                if word[c] ==".":
                    for i in curr.children.values():
                        if dfs(i,word[c+1:]):
                            return True
                    return False
                if word[c] not in curr.children:
                    return False
                curr = curr.children[word[c]]
            
            return curr.isEnd
        return dfs(self.root,word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)