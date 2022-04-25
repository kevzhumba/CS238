from linearDensityValuation import LinearDensityValuation
from valuationInterface import ValuationInterface


class SameLinearDensity(ValuationInterface):
    def __init__(self, n, p):
        self.p = p
        self.valuations = LinearDensityValuation(1, p)

    def noisyCut(self, i: int, lower: float, cutVal: float) -> float:
        return self.valuations.noisyCut(0, lower, cutVal)

    def noisyEval(self, i: int, lower: float, upper: float) -> float:
        return self.valuations.noisyEval(0, lower, upper)

    def getRealValueForAllocation(self, i: int, lower: float, upper: float) -> float:
        return self.valuations.getRealValueForAllocation(0, lower, upper)
    
    def getRealValueForValuation(self, i: int, val: float) -> float:
        return self.valuations.getRealValueForValuation(0, val)