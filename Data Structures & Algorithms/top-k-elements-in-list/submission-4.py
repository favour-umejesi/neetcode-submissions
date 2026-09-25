class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        freq = []
        for key, value in count.items():
            freq.append([value, key])
        
        freq.sort()
        i = 0
        res = []
        while i < k:
            res.append(freq.pop()[1])
            i += 1
        return res


        