class Solution(object):
    def maxFrequencyElements(self, nums):
        a = {}
        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1
        
        max_frequency = max(a.values())  # Get the maximum frequency from the values

        # Step 3: Count elements with maximum frequency
        max_frequency_count = sum(1 for value in a.values() if value == max_frequency)
        
        # Step 4: Calculate total frequencies of elements with maximum frequency
        total_frequency = max_frequency * max_frequency_count
        
        return total_frequency
