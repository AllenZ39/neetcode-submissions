import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = [[] for i in range(len(nums))]
        for num in count:
            bucket[count[num] - 1].append(num)

        solution = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                solution.append(num)
                if len(solution) == k:
                    return solution
