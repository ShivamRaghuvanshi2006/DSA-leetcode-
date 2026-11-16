class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost): return -1
        s=start=0
        for i in range(len(gas)):
            s+=gas[i]-cost[i]
            if s<0: s=0; start=i+1
        return start