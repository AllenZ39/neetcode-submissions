class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        prefix = [None] * len(height)
        suffix = [None] * len(height)
        m = 0
        for i, h in enumerate(height):
            m = max(m, h)
            prefix[i] = m
        m = 0
        for i in range(len(height) - 1, -1, -1):
            m = max(m, height[i])

            suffix[i] = m
        for i, h in enumerate(height):
            area += min(prefix[i], suffix[i]) - h
        return area
