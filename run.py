from cmath import cos
from EvanPaz import EvanPaz
from algorithm import Algorithm
from linearDensityValuation import LinearDensityValuation
from randomSameValuation import RandomSameValuation
import randomValuation
import dubinsSpanier
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

    


print("Random Linear Dubins")
print(runRandomLinearDensityValuationSimulation(10000, 8, 0.01))
print("Random Same Dubins")

print(runRandomSameValuationSimulation(10000, 8, 0.01)) 
print("Random Dubins")

print(runRandomValuationSimulation(10000, 8, 0.01))
print("Random Evans")

print(runRandomValuationSimulationEvan(10000, 8, 0.01))
print("Random Linear Evans")

print(runRandomLinearDensityValuationSimulationEvan(10000, 8, 0.01))
print("Random Same Evans")

print(runRandomSameValuationSimulationEvan(10000, 8, 0.01))

    

            
        