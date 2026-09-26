class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a': 0}
        consonant = {'s': 0}
        for i in s:
            if i in 'aeiou':
                vowels[i] = vowels.get(i, 0) + 1
            else:
                consonant[i] = consonant.get(i, 0) + 1
        return max(vowels.values()) + max(consonant.values())