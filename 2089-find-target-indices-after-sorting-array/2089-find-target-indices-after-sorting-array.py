class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums)
        last = None
        nums.sort()
        ans = []
        while l != r:
            mid = (l + r) // 2
            if mid == last:
                return []
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                left = mid - 1
                while left >= 0 and nums[left] == target:
                    ans.append(left)
                    print(left)
                    left -= 1
                ans.append(mid)
                right = mid + 1
                while right < len(nums) and nums[right] == target:
                    ans.append(right)
                    print(right)
                    right += 1
                break
            last = mid

        return sorted(ans)