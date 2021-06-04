from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) + len(nums2) == 1:
            return nums1[0] if nums1 else nums2[0]

        for ele in nums1 + nums2:
            print(ele)


if __name__ == "__main__":
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([0, 0], [0, 0]) == 0
    assert s.findMedianSortedArrays([], [1]) == 1
    assert s.findMedianSortedArrays([2], []) == 2
