class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        ans = []
        for key, value in freq.items():
            ans.append((value, key))
        ans.sort()

        res = []
        i = 0
        while i < k:
            res.append(ans.pop()[1])
            i += 1
        return res
        