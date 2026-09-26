class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        mc, rn, bc = [], [], []
        for i in nums:
            if i < pivot:
                mc.append(i)
            elif i > pivot:
                bc.append(i)
            else:
                rn.append(i)
        return mc + rn + bc
                