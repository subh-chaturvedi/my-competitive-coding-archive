class Solution:
    def ladderLength(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank: return 0

        queue = deque()
        queue.append((start,1))

        while queue:
            word,steps = queue.popleft()
            if word == end: return steps

            for i,ch in enumerate(word):
                for new_ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + new_ch + word[i+1:]
                    if new_word in bank:
                        queue.append((new_word,steps+1))
                        bank.remove(new_word)

        return 0