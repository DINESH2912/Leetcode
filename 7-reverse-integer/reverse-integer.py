class Solution(object):
    def reverse(self, x):
        mini,maxi=-2**31,2**31-1

        m = str(x)
        if x < 0:
            m = '-' + m[:0:-1]
        else:
            m = m[::-1]

        if int(m)<mini or int(m)>maxi:
            return 0
        return int(m)
