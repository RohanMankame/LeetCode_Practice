class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        Sarr = sorted(nums1+nums2)
        L = int(len(Sarr))
        EP = int((L/2))


        if L % 2 == 0:
            Val = Sarr[EP-1] + Sarr[EP]
            return (Val/2)


        else:
            return(float(Sarr[EP]))
