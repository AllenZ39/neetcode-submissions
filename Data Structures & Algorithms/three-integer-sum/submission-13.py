class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for m in range(1, len(nums)):
            l = 0
            r = len(nums) - 1
            while l < m < r:
                if nums[l] + nums[m] + nums[r] == 0:
                    if [nums[l], nums[m], nums[r]] not in solution:
                        solution.append([nums[l], nums[m], nums[r]])
                   
                if nums[l] + nums[m] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return solution
