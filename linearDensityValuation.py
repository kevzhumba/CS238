import math
from valuationInterface import ValuationInterface
import numpy as np

class LinearDensityValuation(ValuationInterface):
  def __init__(self, n, p):
    self.n = n
    self.p = p
    self.randomNoisyValuations = {}
    for i in range(n):
      randomSlope = np.random.uniform(0, 1)
      randomIntercept = np.random.uniform(0,1)
      totalArea = randomSlope * 0.5 + randomIntercept * 1
      randomSlope = randomSlope/totalArea
      randomIntercept = randomIntercept/totalArea
      self.randomNoisyValuations[i] = (randomSlope, randomIntercept)    
  
  def noisyEval(self, i: int, lower: float, upper: float) -> float:
    (a, b) = self.randomNoisyValuations[i]
    return b * (upper - lower) + a * (upper * upper - lower * lower) / 2
  
  
  def noisyCut(self, i: int, lower: float, cutVal: float) -> float:
    #b * (upper - lower)  = cutVal - a * (upper - lower) * (upper - lower) / 2
    (a, b) = self.randomNoisyValuations[i]
    return (-1 * b  + math.sqrt(b*b + a*a*lower*lower + 2 * a * b * lower + 2 * a * cutVal))/a
    
  
  def getRealValueForAllocation(self, i: int, lower: float, upper: float) -> float:
    noisyVal = self.noisyEval(i, lower, upper)
    x = np.random.uniform(0, 1)
    delta = 1/((1+self.p)-x*(2*self.p))
    return noisyVal * delta

  def getRealValueForValuation(self, i: int, val: float) -> float:
      x = np.random.uniform(0, 1)
      delta = 1/((1+self.p)-x*(2*self.p))
      return val * delta

