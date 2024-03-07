class Solution(object):
    def uniqueOccurrences(self, arr):
        a = {}

        for num in arr:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1
        
        b = set()  # Use a set to store unique counts

        for count in a.values():
            if count in b:
                return False
            else:
                b.add(count)

        return True
