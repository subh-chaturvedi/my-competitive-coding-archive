class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank: return -1

        queue = deque()
        queue.append((start,0))

        while queue:
            word,steps = queue.popleft()
            if word == end: return steps

            for i,ch in enumerate(word):
                for new_ch in "ACGT":
                    new_word = word[:i] + new_ch + word[i+1:]
                    if new_word in bank:
                        queue.append((new_word,steps+1))
                        bank.remove(new_word)

        return -1