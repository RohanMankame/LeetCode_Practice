class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        Count = 0  # keep track of next position to fill starting with inital 0

        for x in range(0, len(nums)):  # loop for all elements in the array nums to check if it is = to val

            if nums[x] != val:  # if not val move to front of array, position kept track using Count
                nums[Count] = nums[x]
                Count = Count + 1  # after element added to front of arr move to next position

        nums = nums[0:Count]  # silce all ellements after the count positon as thay are already gone or are = to val

        return (Count)  # return only count of the elements in num, would be same as the Count or len(nums)
    
 #(OR)
    
    
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:

        while val in nums:
            nums.remove(val)
