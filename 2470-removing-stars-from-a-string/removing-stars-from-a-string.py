class Solution(object):
    def removeStars(self, s):
        k=[]
        for i in range(len(s)):
            if s[i]=='*':
                k.pop()
            else:
                k.append(s[i])
        m=''.join(k)
        return m
        

        