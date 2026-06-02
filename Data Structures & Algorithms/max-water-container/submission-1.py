class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights[0], heights[1])
        i = 0
        j = len(heights) - 1
        area = 0

        while i < j:
            area = max(area, min(heights[i], heights[j]) * (j - i))
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] <= heights[j]:
                i += 1
        return area
