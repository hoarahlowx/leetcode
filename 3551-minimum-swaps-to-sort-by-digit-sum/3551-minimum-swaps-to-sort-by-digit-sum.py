class Solution:
    def digit_sum(self, n: int) -> int:
        n = abs(n)
        total = 0
        while n:
            total += n % 10
            n //= 10
        return total

    def minSwaps(self, nums: List[int]):
        n = len(nums)
        indexed_nums = [[nums[i], i] for i in range(len(nums))]
        indexed_nums.sort(key=lambda item: (self.digit_sum(item[0]), item[0]))
        visited = [False] * n
        c = 0

        for i in range(len(indexed_nums)):
            if visited[i]:
                continue

            c += 1
            temp = i
            while not visited[temp]:
                visited[temp] = True
                temp = indexed_nums[temp][1]

        return n - c