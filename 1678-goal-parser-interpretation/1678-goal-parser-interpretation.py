class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        ln = len(command)
        i = 0
        while i < ln:
            if command[i] == '(' and i + 1 < ln and command[i + 1] == ')':
                ans += 'o'
                i += 1
            elif command[i] not in '()':
                ans += command[i]
            i += 1
        return ans