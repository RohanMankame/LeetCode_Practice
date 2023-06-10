class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pos = 0

        for i in range(0, len(nums)):  # loop all elements from 0 to last element

            currEle = nums[pos]

            if nums[i] != currEle:  # keep skipping numbers if it is the same as the last one
                pos = pos + 1
                nums[pos] = nums[i]
                currEle = nums[i]

        return (
                    pos + 1)  # increase pos by 1 because we were refering to array position before, but we want num of elements
