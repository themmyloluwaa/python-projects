from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            if nums[i] == target:
                pos[i] = target

        pos = list(pos.keys())

        if len(pos) == 0:
            print([-1, -1])
            return [-1, -1]
        else:
            print([pos[0], pos[len(pos) - 1]])
            return [pos[0], pos[len(pos) - 1]]


Solution.searchRange(Solution, [5, 7, 7, 7, 8, 8, 10], 7)
Solution.searchRange(Solution, [5, 7, 7, 8, 8, 10], 6)
