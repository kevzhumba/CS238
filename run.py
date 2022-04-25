from cmath import cos
from EvanPaz import EvanPaz
from algorithm import Algorithm
from linearDensityValuation import LinearDensityValuation
from ourAlgorithm import OurAlgorithm
from randomSameValuation import RandomSameValuation
import randomValuation
import dubinsSpanier
from sameLinearDensity import SameLinearDensity
from valuationInterface import ValuationInterface
import numpy as np

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
    allCosts = []
    for i in range(totalIterations):
        v = randomValuation.RandomValuation(n, p)
        d = dubinsSpanier.DubinsSpanier()
        a = d.runAlg(v, n) 
        cost = getCost(v, a, n) 
        allCosts.append(cost)
        if cost == 0:
            totalSuccess += 1
        else:
            totalFailure += 1
            totalCost += cost
    return (totalSuccess, totalFailure, totalCost/totalIterations, np.var(allCosts))


def runRandomSameValuationSimulation(totalIterations: int, n: int, p: float):
    totalSuccess = 0
    totalFailure = 0
    totalCost = 0
    allCosts = []

    for i in range(totalIterations):
        v = RandomSameValuation(n, p)
        d = dubinsSpanier.DubinsSpanier()
        a = d.runAlg(v, n) 
        cost = getCost(v, a, n) 
        allCosts.append(cost)
        if cost == 0:
            totalSuccess += 1
        else:
            totalFailure += 1
            totalCost += cost

    return (totalSuccess, totalFailure, totalCost/totalIterations, np.var(allCosts))

def runRandomLinearDensityValuationSimulation(totalIterations: int, n: int, p: float):
    totalSuccess = 0
    totalFailure = 0
    totalCost = 0
    allCosts = []

    for i in range(totalIterations):
        v = LinearDensityValuation(n, p)
        d = dubinsSpanier.DubinsSpanier()
        a = d.runAlg(v, n) 
        cost = getCost(v, a, n) 
        allCosts.append(cost)
        if cost == 0:
            totalSuccess += 1
        else:
            totalFailure += 1
            totalCost += cost

    return (totalSuccess, totalFailure, totalCost/totalIterations,np.var(allCosts))


def runRandomLinearDensityValuationSimulationEvan(totalIterations: int, n: int, p: float):
    totalSuccess = 0
    totalFailure = 0
    totalCost = 0
    allCosts = []

    for i in range(totalIterations):
        v = LinearDensityValuation(n, p)
        d = EvanPaz()
        a = d.runAlg(v, n) 
        cost = getCost(v, a, n) 
        allCosts.append(cost)
        if cost == 0:
            totalSuccess += 1
        else:
            totalFailure += 1
            totalCost += cost

    return (totalSuccess, totalFailure, totalCost/totalIterations, np.var(allCosts))

def runRandomValuationSimulationEvan(totalIterations: int, n: int, p:float):
    totalSuccess = 0
    totalFailure = 0
    totalCost = 0
    allCosts = []

    for i in range(totalIterations):
        v = randomValuation.RandomValuation(n, p)
        d = EvanPaz()
        a = d.runAlg(v, n) 
        cost = getCost(v, a, n) 
        allCosts.append(cost)
        if cost == 0:
            totalSuccess += 1
        else:
            totalFailure += 1
            totalCost += cost
    return (totalSuccess, totalFailure, totalCost/totalIterations, np.var(allCosts))


def runRandomSameValuationSimulationEvan(totalIterations: int, n: int, p: float):
    totalSuccess = 0
    totalFailure = 0
    totalCost = 0
    allCosts = []
    for i in range(totalIterations):
        v = RandomSameValuation(n, p)
        d = EvanPaz()
        a = d.runAlg(v, n) 
        cost = getCost(v, a, n) 
        allCosts.append(cost)
        if cost == 0:
            totalSuccess += 1
        else:
            totalFailure += 1
            totalCost += cost

    return (totalSuccess, totalFailure, totalCost/totalIterations, np.var(allCosts))


def runRandomSameValuationSimulationOurAlgorithm(totalIterations: int, m: int, p: float):
    totalSuccess = 0
    totalFailure = 0
    totalCost = 0
    allCosts = []
    for i in range(totalIterations):
        v = LinearDensityValuation(2, p)
        d = OurAlgorithm()
        a = d.runAlgWithMCuts(v, m)
        cost = 0
        for i in range(2):
            allocation = a[i]
            noisyVal = 0
            for (l,u) in allocation:
                noisyVal += v.noisyEval(i, l, u)
            realVal = v.getRealValueForValuation(i, noisyVal)
            if (realVal < 1/2):
                cost += (1/2 - realVal)
        allCosts.append(cost)
        if cost == 0:
            totalSuccess += 1
        else:
            totalFailure += 1
            totalCost += cost

    return (totalSuccess, totalFailure, totalCost/totalIterations, np.var(allCosts))

# print("Random Linear Dubins")
print(runRandomLinearDensityValuationSimulation(10000, 2, 0.1))
# print("Random Same Dubins")

# print(runRandomSameValuationSimulation(10000, 8, 0.2)) 
# print("Random Dubins")

# print(runRandomValuationSimulation(10000, 8, 0.2))
# print("Random Evans")

# print(runRandomValuationSimulationEvan(10000, 8, 0.5))
# print("Random Linear Evans")

print(runRandomLinearDensityValuationSimulationEvan(10000, 2, 0.1))
# print("Random Same Evans")

# print(runRandomSameValuationSimulationEvan(10000, 8, 0.2))

print(runRandomSameValuationSimulationOurAlgorithm(10000, 1000, 0.1))

    

            
        