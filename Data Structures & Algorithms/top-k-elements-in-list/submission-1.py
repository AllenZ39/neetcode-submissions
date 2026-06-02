import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        h = []

        for c in count:
            heapq.heappush(h, (count[c], c))
            if len(h) > k:
                heapq.heappop(h)
        return [num[1] for num in h]

        