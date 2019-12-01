// Interesting things learned
// Order of function declaration matters
// "Pass a 2D array to a function" is not exactly trivial

#include <vector>
using namespace std;

// void printMaxProfit(int **maxprofit, int days, int k){
// 	std::cout << "HELLO";
// }


int maxProfitWithKTransactions(vector<int> prices, int k) {
	if (prices.empty()){
		return 0;
	}
	
	int maxprofit[k+1][prices.size()];
	
	// Initialize to zeros
	for (int i = 0; i < k+1; i++){
		for (int j = 0; j < prices.size(); j++){
			maxprofit[i][j] = 0;
		}
	}
	
	for (int r = 1; r < k+1; r++){
		for (int d = 1; d < prices.size(); d++){
			int maxproflastday = maxprofit[r][d-1];
			
			int maxfound = 0;
			
			for (int x = 0; x < d; x++){
				int found = prices[d] - prices[x] + maxprofit[r-1][x];
				if (found > maxfound){
					maxfound = found;
				}
			}
			
			if (maxfound > maxproflastday){
				maxprofit[r][d] = maxfound;
			}
			else{
				maxprofit[r][d] = maxproflastday;
			}
			 
		}
	}
	
	// printMaxProfit(maxprofit, prices.size(), k);
	
	// Too hard to pass the 2D array haha. Just write it here.
	std::cout << "PRICES:\n";
	for (int i = 0; i < prices.size(); i++){
		std::cout << prices[i] << ", ";
	}
	std::cout << "\n";
	
	std::cout << "MAXPROF:\n";
	for (int i = 0; i < k+1; i++){
		for (int j = 0; j < prices.size(); j++){
			std::cout << maxprofit[i][j] << ", ";
		}
		std::cout << "\n";
	}
	
	std::cout << "ANSWER: " << maxprofit[k][prices.size() - 1] << "\n------\n\n";
	
	return maxprofit[k][prices.size() - 1];
	
}

