class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = {}
        ans = []
        for i in range(len(groupSizes)):
            c = groupSizes[i]
            if c == 1:
                ans.append([i])
            elif c not in groups:
                groups[c] = [i]
            elif len(groups[c]) == c:
                ans.append(groups[c])
                groups[c] = [i]
            else:
                groups[c].append(i)
        for i in groups.values():
            if i != []:
                ans.append(i)
        return ans