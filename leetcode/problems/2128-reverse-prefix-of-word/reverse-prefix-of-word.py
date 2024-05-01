class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x = word.find(ch)
        if x ==-1:
            return word
        else:
            first = word[:x+1]
            first = first[::-1]
            rest = word[x+1:]
            return first+rest