class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            
            #pick1
            backtrack(combination+ phone[next_digits[0]][0], next_digits[1:])
            #pick2
            backtrack(combination+ phone[next_digits[0]][1], next_digits[1:])
            #pick3
            backtrack(combination+ phone[next_digits[0]][2], next_digits[1:])
            #pick4
            if next_digits[0] in ["7","9"]:
                backtrack(combination+ phone[next_digits[0]][3], next_digits[1:])


        backtrack("", digits)
        return res
