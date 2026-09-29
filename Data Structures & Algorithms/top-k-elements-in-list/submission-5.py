from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        {
        1: 1,
        2: 2,
        3: 3,
        }
        [3,2,1] top_k = [3,2] => [3, 2]

        """
        frequency = Counter(nums)
        values = sorted(list(frequency.values()), reverse=True)
        top_k = values[:k]
        result = []

        for key, value in frequency.items():
            if value in top_k:
                result.append(key)

        return result

