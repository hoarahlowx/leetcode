class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        cur1, cur2 = 0, 0
        limit = ((len(nums1) + len(nums2)) // 2) + 1
        t = []
        while cur1 + cur2 < limit:
            if cur1 == len(nums1):
                t.append(nums2[cur2])
                cur2 += 1
            elif cur2 == len(nums2):
                t.append(nums1[cur1])
                cur1 += 1
            elif nums1[cur1] < nums2[cur2]:
                t.append(nums1[cur1])
                cur1 += 1
            elif nums1[cur1] >= nums2[cur2]:
                t.append(nums2[cur2])
                cur2 += 1
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (t[-1] + t[-2]) / 2
        return t[-1]
                
