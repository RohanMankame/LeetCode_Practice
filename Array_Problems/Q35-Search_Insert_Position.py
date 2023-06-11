class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        pos = 0
        for x in range(0, len(nums)):

            if nums[x] == target:
                pos = x
                break

            if nums[x] > target:
                pos = x
                break

            if nums[x] == nums[-1] and nums[-1] < target:
                pos = x + 1
                break

        return pos