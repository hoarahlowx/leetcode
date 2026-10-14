class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        answer = []
        n = len(digits)
        def backtrack(cur, s):
            if len(cur) == n:
                answer.append(cur)
                return
            for i in phone_map[digits[s]]:
                backtrack(cur + i, s + 1)
        backtrack('', 0)
        return answer
                
            