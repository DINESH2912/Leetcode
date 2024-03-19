class Solution(object):
    def countCharacters(self, words, chars):
        sum=0
        for i in words:
            ch=chars
            l=0
            for j in i:
                if j in ch:
                    ch=ch.replace(j,"",1)
                    l+=1
            if l==len(i):
                sum+=len(i)

        return sum