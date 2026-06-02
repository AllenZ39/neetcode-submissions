class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = list(range(len(nums)))
        p = 1
        for i in range(len(nums)):
            m[i] = p
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            m[i] *= p
            p *= nums[i]
        return m