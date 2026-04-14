class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        res = nums[0]
        res_idx = 0

        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] < nums[r]:
                if res > nums[l]:
                    res = nums[l]
                    res_idx = l
                    break

            if res > nums[mid]:
                res = nums[mid]
                res_idx = mid

            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        print(res_idx)

        l, r = 0, res_idx - 1
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1

        if l < res_idx and nums[l] == target:
            return l  

        l, r = res_idx, n - 1
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        if l < n and nums[l] == target:
            return l 
        return -1

