class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights) - 1
        if l == 1:
            return min(heights[0], heights[1])
        i = 0
        j = l
        area = 0

        while i < j:
            area = max(area, min(heights[i], heights[j]) * l)
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else:
                i += 1
            l -= 1
        return area
