from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        tmp_list = []

        for i in range(n):
            other_num = target - nums[i]
            try:
                other_num_index = tmp_list.index(other_num)
                return [other_num_index, i]
            except ValueError:
                tmp_list.append(nums[i])
