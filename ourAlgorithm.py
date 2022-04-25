
import random
from algorithm import Algorithm
from valuationInterface import ValuationInterface

class OurAlgorithm(Algorithm):

    # n = 2
    def runAlgWithMCuts(self, valuations: ValuationInterface, m: int):
        intervals = []
        for i in range(m):
            intervals.append((i/m, (i+1)/m)) 
        random.shuffle(intervals)
        player1Map = {}
        player2Map = {}
        x1 = []
        x2 = []
        player1x1Map = {}
        player2x2Map = {}
        player1x2Map = {}
        player2x1Map = {}
        x1Val = 0
        x2Val = 0
        mu = 0
        y = []
        allocations = {}
        for (l, u) in intervals:
            player1Map[(l,u)] = valuations.noisyEval(0, l, u)
            player2Map[(l,u)] = valuations.noisyEval(1, l, u)
            if player1Map[(l,u)] >= player2Map[(l,u)]:
                player1x1Map[(l,u)] = player1Map[(l,u)]
                player2x1Map[(l,u)] = player2Map[(l,u)]
                x1.append((l,u))
                x1Val += player1Map[(l,u)]
                mu += player2Map[(l,u)]
            else:
                player1x2Map[(l,u)] = player1Map[(l,u)]
                player2x2Map[(l,u)] = player2Map[(l,u)]
                x2.append((l,u))
                x2Val += player2Map[(l,u)]
                mu += player1Map[(l,u)]
        if (x1Val >= x2Val):
            sort_player2_on_x1 = sorted(player2x1Map.items(), key=lambda x: x[1], reverse=True)
            targetVal = x1Val - 3/4 + 1/4 * mu
            currPlayer1YVal = 0
            for ((l, u) , v) in sort_player2_on_x1:
                y.append((l,u))
                currPlayer1YVal += (player1Map[(l,u)])
                if (currPlayer1YVal >= targetVal):
                    break
            #now, we have y, so we want to give X1/y to player 1 and X2 U Y to player 2
            allocations[0] = list(filter(lambda a: not (a in y), x1))
            allocations[1] = x2 + y
            return allocations
        else:
            sort_player1_on_x2 = sorted(player1x2Map.items(), key=lambda x: x[1], reverse=True)
            targetVal = x2Val - 3/4 + 1/4 * mu
            currPlayer2YVal = 0
            for ((l, u) , v) in sort_player1_on_x2:
                y.append((l,u))
                currPlayer2YVal += (player2Map[(l,u)])
                if (currPlayer2YVal >= targetVal):
                    break
            allocations[0] = x1 + y
            allocations[1] = list(filter(lambda a: not (a in y), x2))
            return allocations

    def runAlg(self, valuations: ValuationInterface, n: int):
        return super().runAlg(valuations)