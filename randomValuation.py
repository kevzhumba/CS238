import numpy as np
from valuationInterface import ValuationInterface

#num players

class RandomValuation(ValuationInterface):
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.realMap = {}
        self.noisyMap = {}
        for i in range(n):
            self.realMap[i] = {(0,1) : 1}
            self.noisyMap[i] = {(0,1) : 1}

    def chooseNewValsForAdjacentIntervals(self, playerNoisyMap, startingInterval, endingInterval, totalVal, lower, upper, cutVal):
        if (startingInterval == endingInterval):
            interval1 = (startingInterval[0], lower)
            interval2 = (upper, startingInterval[1])
            interval1val = np.random.uniform(0, playerNoisyMap[startingInterval] - cutVal)
            if (startingInterval[0] == lower):
                interval1val = 0
            interval2val = playerNoisyMap[startingInterval] - cutVal - interval1val
            playerNoisyMap.pop(startingInterval, None)
            playerNoisyMap.pop(endingInterval, None)
            if (startingInterval[0] != lower):
                playerNoisyMap[interval1] = interval1val
            playerNoisyMap[interval2] = interval2val
            playerNoisyMap[(lower, upper)] = cutVal

        else:
            interval1 = (startingInterval[0], lower)
            interval2 = (lower, startingInterval[1])
            interval3 = (endingInterval[0], upper)
            interval4 = (upper, endingInterval[1])
            betweenIntervalVal = totalVal - playerNoisyMap[startingInterval] - playerNoisyMap[endingInterval]
            #intuitively, don't put so little into interval2 s.t. the interval3 can't contain the rest 
            lowerBound = max(cutVal-betweenIntervalVal-playerNoisyMap[endingInterval], 0)
            #and don't put so much value into interval2 s.t. the entire starting interval can't hold it 
            upperBound = min(cutVal-betweenIntervalVal, playerNoisyMap[startingInterval])
            interval2val = np.random.uniform(lowerBound, upperBound)
            if (lower == startingInterval[0]):
                interval2val = playerNoisyMap[startingInterval]
            interval3val = cutVal - betweenIntervalVal - interval2val
            if (upper == endingInterval[1]):
                interval3val = playerNoisyMap[endingInterval]
                interval2val = cutVal - betweenIntervalVal - interval3val
            interval1val = playerNoisyMap[startingInterval] - interval2val
            interval4val = playerNoisyMap[endingInterval] - interval3val
            playerNoisyMap.pop(startingInterval, None)
            playerNoisyMap.pop(endingInterval, None)
            if (lower != startingInterval[0]):
                playerNoisyMap[interval1] = interval1val
            if (upper != endingInterval[1]):
                playerNoisyMap[interval4] = interval4val 
            playerNoisyMap[interval2] = interval2val
            playerNoisyMap[interval3] = interval3val
        return playerNoisyMap

    def noisyEval(self, i: int, lower: float, upper: float) -> float:  
        playerNoisyMap = self.noisyMap[i]
        startingInterval = (0,1)
        endingInterval = (0,1) 
        if (lower == upper or lower == 1):
            return 0

        for (l,u) in playerNoisyMap.keys():
            #find the interval for lower, if lower is at the edge it is correct to take the upper interval
            if (l <= lower and u > lower):
                startingInterval = (l,u)
            #find the interval for upper, if upper is at the edge it is correct to take the lower interval
            if (l < upper and u >= upper):
                endingInterval = (l,u)  

        currInterval = startingInterval
        totalVal = playerNoisyMap[startingInterval]
        a = False
        while (currInterval != endingInterval):
            #search for the "next" interval
            for (l,u) in playerNoisyMap.keys():
                a = True
                if (currInterval[0] == currInterval[1]):
                    raise Exception("die")
                if (currInterval[1] == l):
                    a = False
                    currInterval = (l,u)
                    totalVal += playerNoisyMap[(l,u)]
                    break
            if a:
                raise Exception("die")

        if (lower == startingInterval[0] and upper == endingInterval[1]):
            return totalVal

        #in this case, the lower bound should be the starting interval
        if (lower == startingInterval[0] and startingInterval != endingInterval):
            evalReturn = np.random.uniform(max(totalVal - playerNoisyMap[startingInterval] - playerNoisyMap[endingInterval], playerNoisyMap[startingInterval]), totalVal)
        elif (upper == endingInterval[1] and startingInterval != endingInterval):
            evalReturn = np.random.uniform(max(totalVal - playerNoisyMap[startingInterval] - playerNoisyMap[endingInterval], playerNoisyMap[endingInterval]), totalVal)
        else: 
            #max handles the case of starting and ending being the same (in that case, min poll value is 0)
            evalReturn = np.random.uniform(max(totalVal - playerNoisyMap[startingInterval] - playerNoisyMap[endingInterval], 0), totalVal)
        self.noisyMap[i] = self.chooseNewValsForAdjacentIntervals(playerNoisyMap, startingInterval, endingInterval, totalVal, lower, upper, evalReturn)
        return evalReturn

    def noisyCut(self, i: int, lower: float, cutVal: float) -> float:
        #edge case handling for end of cake, since we check that the upper bound is strictly greater than
        if (cutVal == 0):
            return lower
        if (lower == 1):
            if (cutVal != 0):
                return -1
            else:
                return 1
        playerNoisyMap = self.noisyMap[i]

        startingInterval = (0,1)
        for (l,u) in playerNoisyMap.keys():
            #find the interval where lower begins
            if (l <= lower and u > lower):
                startingInterval = (l,u)
                break
        
        intervalVal = playerNoisyMap[startingInterval]
        totalVal = intervalVal
        #at the end of the loop, this will hold the end interval
        currInterval = startingInterval
        a = False
        while ((lower != startingInterval[0] and totalVal <= cutVal) or totalVal < cutVal):
            #find the partition that is the next interval
            if (currInterval[1] == 1):
                return -1
            for (l1,u1) in playerNoisyMap.keys():
                a = True
                if (currInterval[0] == currInterval[1] or l1 == u1):
                    raise Exception("die")
                if (l1 == currInterval[1]):
                    a = False
                    totalVal += playerNoisyMap[(l1, u1)]
                    currInterval = (l1, u1)
                    break
            if a :
                raise Exception("die")
        #if the total value is the cut value and lower is equal to startingInterval[0], then we just return (startingInterval[0], currInterval[1])
        if (totalVal == cutVal and lower == startingInterval[0]):
            return currInterval[1]

        #otherwise, at this point, we want to poll for a point in currInterval
        cutPoint = np.random.uniform(low = currInterval[0], high = currInterval[1])
        while (cutPoint == currInterval[0]):
            cutPoint = np.random.uniform(low = currInterval[0], high = currInterval[1])

        self.noisyMap[i] = self.chooseNewValsForAdjacentIntervals(playerNoisyMap, startingInterval, currInterval, totalVal, lower, cutPoint, cutVal)
        return cutPoint

    def getRealValueForAllocation(self, i: int, lower: float, upper: float) -> float:
        playerNoisyMap = self.noisyMap[i]
        noisyVal = self.noisyEval(i, lower, upper)
        x = np.random.uniform(0, 1)
        delta = 1/((1+self.p)-x*(2*self.p))
        return noisyVal * delta

    def getRealValueForValuation(self, i: int, val: float) -> float:
        x = np.random.uniform(0, 1)
        delta = 1/((1+self.p)-x*(2*self.p))
        return val * delta

        

        











    





                        
                



