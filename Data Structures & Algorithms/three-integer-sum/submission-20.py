class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for m in range(1, len(nums) - 1):
            if nums[m] == nums[m - 1]:
                if m > 1 and nums[m] == nums[m - 2]:
                    continue
                l = m - 1
            else:
                l = 0
            r = len(nums) - 1
            while l < m < r:
                total = nums[l] + nums[m] + nums[r]
                if total == 0:
                    solution.append([nums[l], nums[m], nums[r]])
                    l += 1
                    r -= 1
                    while l < m and nums[l] == nums[l - 1]:
                        l += 1
                    
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return solution
