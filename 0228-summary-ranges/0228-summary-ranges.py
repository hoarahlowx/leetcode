class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if nums == []:
            return []
        et = nums[0]
        ans = []
        dep = 0
        for i in nums[1:]:
            if i - et == dep + 1:
                dep += 1
            else:
                if dep == 0:
                    ans.append(str(et))
                else:
                    ans.append(f'{et}->{et+dep}')
                    dep = 0
                et = i
        if dep == 0:
            ans.append(str(et))
        else:
            ans.append(f'{et}->{et+dep}')
            dep = 0
        return ans