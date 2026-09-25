class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            bucket[value].append(key)

        n = len(nums)
        ans = []
        for i in range(n, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        # for key, value in freq.items():
        #     ans.append((value, key))
        # ans.sort()

        # res = []
        # i = 0
        # while i < k:
        #     res.append(ans.pop()[1])
        #     i += 1
        # return res
        