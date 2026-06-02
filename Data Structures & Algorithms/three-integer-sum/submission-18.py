class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = set()
        nums.sort()
        for m in range(1, len(nums)):
            l = 0
            r = len(nums) - 1
            while l < m < r:
                total = nums[l] + nums[m] + nums[r]
                if total == 0:
                    solution.add((nums[l], nums[m], nums[r]))
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return [list(t) for t in solution]
