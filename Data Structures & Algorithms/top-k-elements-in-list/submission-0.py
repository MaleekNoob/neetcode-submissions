from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_counter[:k]]