from cmath import cos
from algorithm import Algorithm
from randomSameValuation import RandomSameValuation
import randomValuation
import dubinsSpanier
from valuationInterface import ValuationInterface

def getCost(v: ValuationInterface, a, n):
    cost = 0
    for i in range(n):
        allocation = a[i]
        realVal = v.getRealValueForAllocation(i, allocation[0], allocation[1])
        if (realVal < 1/n):
            cost += (1/n - realVal)
    return cost

def runRandomValuationSimulation(totalIterations: int, n: int, p:float):
    totalSuccess = 0
    totalFailure = 0
    totalCost = 0
    for i in range(totalIterations):
        v = randomValuation.RandomValuation(n, p)
        d = dubinsSpanier.DubinsSpanier()
        a = d.runAlg(v, n) 
        cost = getCost(v, a, n) 
        if cost == 0:
            totalSuccess += 1
        else:
            totalFailure += 1
            totalCost += cost
    return (totalSuccess, totalFailure, totalCost/totalIterations)


def runRandomSameValuationSimulation(totalIterations: int, n: int, p: float):
    totalSuccess = 0
    totalFailure = 0
    totalCost = 0
    for i in range(totalIterations):
        v = RandomSameValuation(n, p)
        d = dubinsSpanier.DubinsSpanier()
        a = d.runAlg(v, n) 
        cost = getCost(v, a, n) 
        if cost == 0:
            totalSuccess += 1
        else:
            totalFailure += 1
            totalCost += cost

    return (totalSuccess, totalFailure, totalCost/totalIterations)

#print(runRandomSameValuationSimulation(100000, 10, 0.002)) TODO this is broken because of floating point rounding
print(runRandomValuationSimulation(10000, 10, 0.01))

    

            
        