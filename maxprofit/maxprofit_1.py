# -*- coding: utf-8 -*-
"""
Demo problem from https://www.algoexpert.io/questions/Max%20Profit%20With%20K%20Transactions
This is my first solution without looking for help
Time: 1hr:30m
"""

def maxProfitWithKTransactions(prices, k):
    # Write your code here.

    # In the case of a two peak distribution, two transactions is the maximum needed. More transactions doesn't help.

    # In the case there are more peaks than transactions, then they have to be combined into a single transaction in the best possible way

    # k = 1 case, just buy the minimum and sell at the maximum
    # print(f"prices: {prices}, k: {k}")

    if len(prices) == 0 or k == 0:
        return 0

    peak_runs = get_peak_runs(prices)
    # print(f"peak_runs: {peak_runs}")
    if k >= len(peak_runs):
        return sum([j - i for i, j in peak_runs])

    # Now need to find the optimum choices to combine, have to be next to each other to combine them
    else:
        # it's a linear reduction so just choose in order of the least reduction until k is satisfied

        combined_peak_runs = get_optimally_combined_peak_runs(peak_runs, k)
        return sum([j - i for i, j in combined_peak_runs])


def get_optimally_combined_peak_runs(peak_runs, k):
    """ Combine peak runs given number of runs k

    >>> get_optimally_combined_peak_runs([5, 20, 3, 50, 40, 90], 1)
    [(3, 90)]

    >>> get_optimally_combined_peak_runs([5, 20, 3, 50, 40, 90], 2)
    # [(3, 50), (40, 90)] is 97
    # [(5, 50), (40, 90)] is 95
    # [(5, 20), (3, 90)] is 102
    """
    # Just brute force it for now...
    # Iterate through the ones touching each other and find the best one to combine, repeat if the length is not k
    if peak_runs == None or peak_runs == []:
        return []

    best_found_peak_runs = peak_runs[:-1]  # Toss the last out, claim this is the best until better is found
    best_found_sum = sum([j - i for i, j in best_found_peak_runs])

    for i in range(len(peak_runs) - 1):
        # For each peak run, what's better, combining with the next or tossing? Of the best option, keep track of the global best
        # The last element cannot be combined with anything, however it has already been considered to start the comparison loop
        run = peak_runs[i]
        nextrun = peak_runs[i + 1]

        tossscore = nextrun[1] - nextrun[0]
        combinescore = nextrun[1] - run[0]

        if combinescore > tossscore:
            candidate = (run[0], nextrun[1])
        else:
            candidate = (nextrun[0], nextrun[1])

        candidate_peak_runs = peak_runs[:i] + [candidate] + peak_runs[i + 2:]
        candidate_sum = sum([j - i for i, j in candidate_peak_runs])
        if candidate_sum > best_found_sum:
            best_found_sum = candidate_sum
            best_found_peak_runs = candidate_peak_runs

    # Recursively solve this linear problem until it has been reduced to k peak runs
    if len(best_found_peak_runs) == k:
        return best_found_peak_runs
    else:
        return get_optimally_combined_peak_runs(best_found_peak_runs, k)


def get_peak_runs(prices):
    """ A peak run is from a minimum amount to a maximum amount

    >>> get_peak_runs([5, 11, 3, 50, 60, 90])
    [(5, 11), (3, 90)]

    >>> get_peak_runs([5, 11, 6, 3, 7, 90])
    [(5, 11), (3, 90)]
    """
    peak_runs = []
    lastprice = prices[0]
    localmin = prices[0]
    localmax = prices[0]
    for i in range(1, len(prices)):
        # is price going up or down?
        currentprice = prices[i]
        lastprice = prices[i - 1]

        # price going up
        if currentprice > lastprice:
            localmax = currentprice
            # If at the end, make sure to add this run on
            if i == len(prices) - 1:
                peak_runs.append((localmin, localmax))

        # price going down
        if currentprice < lastprice:
            # append previous peak run to list if there is a net gain
            if localmax > localmin:
                peak_runs.append((localmin, localmax))
            localmin = currentprice
            localmax = currentprice

    return peak_runs

