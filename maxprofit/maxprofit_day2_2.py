# -*- coding: utf-8 -*-
"""
Demo problem from https://www.algoexpert.io/questions/Max%20Profit%20With%20K%20Transactions
This is day 2 after watching the video and studying how to solve it

Notebook Time: 18:40
Coding Time: 3:56
"""


# First attempt, had an error which was found in 10 or so seconds
def maxProfitWithKTransactions(prices, k):
    maxprof = [[0] * len(prices) for _ in range(k + 1)]
    for r in range(1, k + 1):
        for d in range(1, len(prices)):
            maxprof[r][d] = max(
                maxprof[r][d-1],
                max(
                    [prices[d] - prices[x] + maxprof[r-1][d] for x in range(d)]
                )
            )
    return maxprof[-1][-1]


# Second attempt
def maxProfitWithKTransactions_2(prices, k):
    if not prices:
        return 0
    maxprof = [[0] * len(prices) for _ in range(k + 1)]
    for r in range(1, k + 1):
        for d in range(1, len(prices)):
            maxprof[r][d] = max(
                maxprof[r][d - 1],
                max(
                    [prices[d] - prices[x] + maxprof[r - 1][x] for x in range(d)]
                )
            )
    return maxprof[-1][-1]