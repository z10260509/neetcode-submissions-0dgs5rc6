class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        if nums[l] <= nums[r]:
            return nums[l]
    
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < nums[(mid - 1) ]:
                return nums[mid]
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid -1

