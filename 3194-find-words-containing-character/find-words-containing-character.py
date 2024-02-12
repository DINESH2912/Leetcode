class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        b=[]
        for i in range(len(words)):
            if x in words[i]:
                b.append(i)
            else:
                pass
        return b
            


        