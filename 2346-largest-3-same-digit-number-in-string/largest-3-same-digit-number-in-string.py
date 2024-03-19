class Solution(object):
    def largestGoodInteger(self, num):
        a = {}
        for i in range(len(num) - 2):
            sub = num[i:i + 3]
            if sub[0] == sub[1] == sub[2]:
                if sub not in a:
                    a[sub] = 1
                else:
                    a[sub] += 1

        max_good_integer = max(a.keys()) if a else ""
        return max_good_integer