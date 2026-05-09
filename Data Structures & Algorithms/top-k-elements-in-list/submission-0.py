class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in hashmap.items():
            buckets[freq].append(num)
        result = []
        for n in range(len(nums), 0, -1):
            for num in buckets[n]:
                result.append(num)
                if len(result) == k:
                    return result