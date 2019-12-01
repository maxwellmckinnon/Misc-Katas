# -*- coding: utf-8 -*-
"""
Demo problem from https://www.algoexpert.io/questions/Max%20Profit%20With%20K%20Transactions
This is day 2 after watching the video

After notebooking out my solution, it seems it is O(n) and faster. Where is it not faster? Let's find out

Notebook Time: 2hr
Coding Time: 1hr
"""

# O(n^2 k)
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if len(prices) == 0 or prices == None:
        return 0

    profits = [[0] * len(prices) for i in range(k + 1)]  # initialize empty 2D array, dimensions len(prices) x k

    for t in range(1, k + 1):
        for d in range(1, len(prices)):
            profits[t][d] = max(
                profits[t][d - 1],
                prices[d] + max(
                    [profits[t - 1][x] - prices[x] for x in range(d)]
                )
            )
    return profits[-1][-1]



# O(n k)
def maxProfitWithKTransactions_faster(prices, k):
    # Write your code here.
    if len(prices) == 0 or prices == None:
        return 0


    profits = [[0] * len(prices) for i in range(k + 1)]  # initialize empty 2D array, dimensions len(prices) x k

    for t in range(1, k + 1):
        maxsofar = float('-inf')
        for d in range(1, len(prices)):
            newmax = profits[t - 1][d - 1] - prices[d - 1]
            if newmax > maxsofar:
                maxsofar = newmax

            profits[t][d] = max(
                profits[t][d - 1],
                prices[d] + maxsofar
            )
    return profits[-1][-1]



# Reduce Space complexity to O(n)
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if len(prices) == 0 or prices == None:
        return 0


    profits_1 = [0] * len(prices)  # empty 1D array
    profits_2 = [0] * len(prices)  # empty 1D array

    for t in range(1, k + 1):
        maxsofar = float('-inf')
        if t % 2 == 0:
            profits = profits_1
            profits_old = profits_2
        else:
            profits = profits_2
            profits_old = profits_1

        for d in range(1, len(prices)):
            newmax = profits_old[d - 1] - prices[d - 1]
            if newmax > maxsofar:
                maxsofar = newmax

            profits[d] = max(
                profits[d - 1],
                prices[d] + maxsofar
            )
    return profits[-1]
