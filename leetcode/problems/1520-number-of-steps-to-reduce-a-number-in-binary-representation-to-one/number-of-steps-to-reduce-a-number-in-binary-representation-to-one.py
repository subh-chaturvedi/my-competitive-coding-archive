class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        n = len(s) - 1
        for i in range(n, 0, -1):
            if int(s[i]) + carry == 1:
                print(int(s[i]) + carry)
                carry = 1
                steps += 2
            else:
                print(int(s[i]) + carry)
                steps += 1
        return steps + carry

        