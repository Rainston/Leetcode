class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
            # Find the maximum frequency
        max_freq = max(freq.values()) if freq else 0
    
    # Count how many elements have maximum frequency
        count_max_freq = sum(1 for f in freq.values() if f == max_freq)
    
    # Multiply the maximum frequency by the count of elements having it
        return max_freq * count_max_freq