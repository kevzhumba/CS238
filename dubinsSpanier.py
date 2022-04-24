from algorithm import Algorithm


class DubinsSpanier(Algorithm):    
    def runAlg(self, valuations, n):
        worklist = set()
        allocations = []
        allocationMap = {}
        latestCut = 0
        for i in range(n):
            worklist.add(i)
        while (len(worklist) != 1):
            earliestPlayer = -1
            earliestCut = 2
            for i in worklist:
                cutForI = valuations.noisyCut(i, latestCut, 1/n)
                if (cutForI < 0):
                    raise Exception("die")
                if (cutForI < earliestCut):
                    earliestPlayer = i
                    earliestCut = cutForI
                
            allocations.append((latestCut, earliestCut))
            allocationMap[earliestPlayer] = (latestCut, earliestCut)
            latestCut = earliestCut
            worklist.remove(earliestPlayer)
        e = next(iter(worklist))
        allocationMap[e] = (latestCut, 1)
        return allocationMap



        
        



            

        


