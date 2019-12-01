//
// Notebook Time: 0
// Coding Time: 1hr
// New things:
// 2D array notation is [,], concept of jaggedarrays
// Static typing
// Int32.MaxInt didn't work as expected?
// Not quite sure how to print things cleanly, are there no builtins to print an array?

using System;
using System.IO;

public class Program {
	public static int MaxProfitWithKTransactions(int[] prices, int k) {
		if (prices.Length == 0)
		{
			return 0;
		}
		
		int[,] maxprof = new int[k+1, prices.Length];  // initialize 2D array of 0's
		
		for (int r = 1; r < k + 1; r++)
		{
			for (int d = 1; d < prices.Length; d++)
			{
				int previousdaymaxprofit = maxprof[r, d-1];
				
				int maxfound = -9999;
				for (int i = 0; i < d; i++)  // Loop through to find maximum price
				{
					int val = prices[d] - prices[i] + maxprof[r-1, i];
					if (val > maxfound)
					{
						maxfound = val;
					}
				}
				
				if (previousdaymaxprofit > maxfound)
				{
					maxprof[r, d] = previousdaymaxprofit;
				}
				else
				{
					maxprof[r, d] = maxfound;
				}

			}
		}
		
		printprices(prices);
		printmaxprof(maxprof, prices.Length);
		return maxprof[k, prices.Length-1];
	}
	
	public static void printprices(int[] prices) {
		Console.WriteLine("Prices:");
		for (int i = 0; i < prices.Length - 1; i++)
		{
			Console.Write(prices[i].ToString());
			Console.Write(", ");
		}
		Console.Write(prices[prices.Length - 1]);
		Console.Write("\n\n");
	}
	
	public static void printmaxprof(int[,] maxprof, int days) {
		Console.WriteLine("Maxprof:");
		Console.WriteLine(maxprof.Length);
		int k = maxprof.Length / days;
		for (int i = 0; i < k; i++)
		{
			for (int d = 0; d < days; d++)
			{
				Console.Write(maxprof[i,d]);
				Console.Write(", ");
			}
			Console.WriteLine();
		}
		Console.WriteLine();
	}
	
}

