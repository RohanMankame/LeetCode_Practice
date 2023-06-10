class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for x in range(0, len(nums)):
            for y in range(0, len(nums)):
                if x == y:
                    break

                currT = nums[x] + nums[y]

                if currT == target:
                    return ([x, y])
