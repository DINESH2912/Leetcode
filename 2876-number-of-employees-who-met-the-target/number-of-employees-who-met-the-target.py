class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        con=0
        for i in range(len(hours)):
            if hours[i]>=target:
                con+=1
            else:
                pass
        return con
        