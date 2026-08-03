class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        iterate through the list, the idx is the freq of that number
        iterate through freq list from the back, adding to res until len = k
        return res
        """
        counts = defaultdict(int)
        freq = [ [] for x in range(len(nums)+1) ]
        for num in nums:
            counts[num] += 1

        for num in list(counts.keys()):
            freq[counts[num]].append(num)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res