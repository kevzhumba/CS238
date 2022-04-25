from randomValuation import RandomValuation
from valuationInterface import ValuationInterface


class RandomSameValuation(ValuationInterface):
    def __init__(self, n, p) -> None:
        self.v = RandomValuation(n, p)

    def noisyCut(self, i: int, lower: float, cutVal: float) -> float:
        return self.v.noisyCut(0, lower, cutVal)
    
    def noisyEval(self, i: int, lower: float, upper: float) -> float:
        return self.v.noisyEval(0, lower, upper)
     
    def getRealValueForAllocation(self, i: int, lower: float, upper: float) -> float:
        return self.v.getRealValueForAllocation(0, lower, upper)

    def getRealValueForValuation(self, i: int, val: float) -> float:
        return self.v.getRealValueForValuation(i, val)
    

    