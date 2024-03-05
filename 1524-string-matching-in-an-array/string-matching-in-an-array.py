class Solution(object):
    def stringMatching(self, words):
        t=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[i] in words[j] and words[i] not in t :
                    t.append(words[i])
                else:
                    pass

        return t


        