class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        1) Create a dictionary to store the frequency of each value
        2) create a list to store values and their count, then sort the list.
        3) Create another list to store the k most frequent numbers, using a while loop,
        set a condition that while the length of the list is less than k, add the value at index 1 of the list
        till it meets the condition
        4) return list
        """

        seen = {}

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        res = []

        for n, v in seen.items():
            res.append([v,n])
        
        res.sort()
        

        freq = []

        while len(freq) < k:
            freq.append(res.pop()[1])

        return freq




        