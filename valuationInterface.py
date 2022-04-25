class ValuationInterface:
    def noisyEval(self, i: int, lower: float, upper: float) -> float:
        pass

    def noisyCut(self, i: int, lower: float, cutVal: float) -> float:
        pass    

    def getRealValueForAllocation(self, i: int, lower: float, upper: float) -> float:
        pass
    
    def getRealValueForValuation(self, i: int, val: float) -> float:
        pass
