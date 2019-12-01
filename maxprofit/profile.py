"""
Profile my first answer against given answers
"""

from timeit import timeit

from maxprofit_1 import maxProfitWithKTransactions as maxProfitWithKTransactions_max
from maxprofit_2 import maxProfitWithKTransactions as maxProfitWithKTransactions_2
from maxprofit_2 import maxProfitWithKTransactions_lessmemory as maxProfitWithKTransactions_2_lessmem


prices_test = [1, 100, 101, 200, 201, 300, 301, 400, 401, 500]
k = 5
prices_answer = 499


# ~This is clunky, just use ipython %%timeit
# timeit('maxProfitWithKTransactions_max(prices_test, k)')
#
# timeit('maxProfitWithKTransactions_2(prices_test, k)')
#
# timeit('maxProfitWithKTransactions_2_lessmem(prices_test, k)')


# prices_test = [1, 100, 101, 200, 201, 300, 301, 400, 401, 500]
#    ...: k = 5
#    ...: prices_answer = 499
#
# In [4]: %timeit maxProfitWithKTransactions(prices_test, k)
# 2.29 µs ± 13.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#
# In [7]: %timeit maxProfitWithKTransactions_2(prices_test, k)
# 28.7 µs ± 576 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#
# In [8]: %timeit maxProfitWithKTransactions_2_lessmem(prices_test, k)
# 24.3 µs ± 306 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)


# In [15]: prices_test = [random.randint(0,1000) for i in range(1000)]
#
# In [16]: k = 50
#
# In [17]: %timeit maxProfitWithKTransactions(prices_test, k)
# 797 ms ± 18.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#
# In [18]: %timeit maxProfitWithKTransactions_2(prices_test, k)
# 31.4 ms ± 2.4 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
#
# In [19]: %timeit maxProfitWithKTransactions_2_lessmem(prices_test, k)
# 25.8 ms ± 398 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)