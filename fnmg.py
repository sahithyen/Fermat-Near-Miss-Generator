#!/usr/bin/env python3
import math
import json

# A near miss generator for Fermat's Last Theorem
# a^n + b^n = c^n (n > 2)

# Min/max value of 'a', 'b' and 'c'
startNumber = 1000
stepSize = 1000
searchSize = 3000
maxMiss = 1e-08
iterations = 20

# Min/max number 'n'
minN = 12
maxN = 22

# 'c' should not be near 'a' and 'b' by this value
diffCToAB = 20


# Get's the nearest solution for a given range for the base and given exponent
def getNearestSolution(minB, maxB, n):
    nearestSolution = {
        'a': 0,
        'b': 0,
        'c': 0,
        'n': 0,
        'miss': 1
    }

    nMiss = 1
    for a in range(minB, maxB + 1):
        for b in range(a, maxB + 1):
            cExact = math.pow(math.pow(a, n) + math.pow(b, n), 1.0 / n)
            miss = cExact % 1

            if miss > 0.5:
                cExact += 1
                miss = 1 - miss
                pass

            if miss < nMiss:
                c = int(math.floor(cExact))

                if c > b + diffCToAB and c > a + diffCToAB:
                    nearestSolution = {
                        'a': a,
                        'b': b,
                        'c': int(math.floor(cExact)),
                        'n': n,
                        'miss': miss
                    }

                    nMiss = miss
                    pass

                pass

            pass

        pass

    return nearestSolution

solutions = []
for iteration in range(0, iterations):
    minB = startNumber + iteration * stepSize
    maxB = minB + searchSize

    print("Iteration " + str(iteration + 1) + " started")

    for n in range(minN, maxN + 1):
        solution = getNearestSolution(minB, maxB, n)
        print("Nearest solution for the bases between " + str(minB) + " and " +
              str(maxB) + " and the exponent " + str(n) + " => " +
              str(solution))

        if solution['miss'] < maxMiss:
            solutions.append(solution)
            pass

        pass

    pass

with open('solutions.json', 'w') as sf:
    json.dump(solutions, sf)
