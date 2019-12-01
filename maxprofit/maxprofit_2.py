# -*- coding: utf-8 -*-
"""
Demo problem from https://www.algoexpert.io/questions/Max%20Profit%20With%20K%20Transactions

This is a solution copying from answer
"""

# O(nk) time | O(nk) space
def maxProfitWithKTransactions(prices, k):
    if not len(prices):
        return 0
    profits = [[0 for d in prices] for t in range(k + 1)]
    for t in range(1, k + 1):
        maxThusFar = float('-inf')
        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
            profits[t][d] = max(profits[t][d - 1], maxThusFar + prices[d])
    return profits[-1][-1]


# Replace 2D array with two 1D arrays
# O(nk) time | O(n) space
def maxProfitWithKTransactions_lessmemory(prices, k):
    if not len(prices):
        return 0
    evenProfits = [0 for d in prices]
    oddProfits = [0 for d in prices]
    for t in range(1, k + 1):
        maxThusFar = float('-inf')
        if t % 2 == 1:
            currentProfits = oddProfits
            previousProfits = evenProfits
        else:
            currentProfits = evenProfits
            previousProfits = oddProfits
        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d - 1])
            currentProfits[d] = max(currentProfits[d - 1], maxThusFar + prices[d])
    return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]
