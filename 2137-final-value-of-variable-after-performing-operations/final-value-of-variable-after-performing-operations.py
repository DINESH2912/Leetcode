class Solution(object):
    def finalValueAfterOperations(self, operations):
        a=[]
        for i in range(0,len(operations)):
            if "--X" in operations[i]:
                a.append(-1)
            if "X--" in operations[i]:
                a.append(-1)
            if "X++" in operations[i]:
                a.append(1)
            if "++X" in operations[i]:
                a.append(1)
        return sum(a)

        