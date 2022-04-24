from numpy import sort
from algorithm import Algorithm
from valuationInterface import ValuationInterface


class EvanPaz(Algorithm):    
    def runAlg(self, valuations: ValuationInterface, n):
        players = set()
        for i in range(n):
            players.add(i)
        return self.runAlgHelper(valuations, 0, 1, players)

      

    def runAlgHelper(self, valuations: ValuationInterface, starting, ending, players):
        cutList = []
        cutMap = {}
        allocations = {}
        if len(players) == 1:
            for i in players:
                allocations[i] = (starting, ending)
                return allocations
        for i in players:
            cutLoc = valuations.noisyCut(i, starting, 1/2 * valuations.noisyEval(i, starting, ending))
            if (cutLoc < 0): 
              raise Exception("Die")
            cutMap[i] = cutLoc
            cutList.append(cutMap[i])
        sort_cuts = sorted(cutMap.items(), key=lambda x: x[1], reverse=False)
        middleIndex = len(players)//2
        newUpperStarting = sort_cuts[middleIndex-1][1]
        lowerHalf = sort_cuts[:middleIndex]
        upperHalf = sort_cuts[middleIndex:]
        lowerPlayers = set()
        for (i, c) in lowerHalf:
            lowerPlayers.add(i)
        upperPlayers = set()
        for (i, c) in upperHalf:
            upperPlayers.add(i)
        lowerAllocations = self.runAlgHelper(valuations, starting, newUpperStarting, lowerPlayers)
        upperAllocations = self.runAlgHelper(valuations, newUpperStarting, ending, upperPlayers)
        return {**lowerAllocations, **upperAllocations}

        


