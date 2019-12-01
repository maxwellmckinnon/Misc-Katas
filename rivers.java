// Things learned
// Seems very C++ like
// I liked that arrays printed out without extra work
// Passing around 2D arrays also seemed easily done
// Notebook time: 10 min
// Coding time: 32 min

import java.util.*;
import java.io.*;

class Program {
  public static List<Integer> riverSizes(int[][] matrix) {
    Integer height = matrix.length;
		Integer width = matrix[0].length;
		int[][] searched = new int[height][width];  // not sure on order here
		
		
		for (int i = 0; i < height; i++){
			for (int j = 0; j < width; j++){
				searched[i][j] = 0;
			}
		}
		
		List<Integer> found = new ArrayList<Integer>();
		for (int i = 0; i < height; i++){
			for (int j = 0; j < width; j++){
				if (searched[i][j] == 1) {
					continue;
				}
				if (matrix[i][j] == 0){
					searched[i][j] = 1;
					continue;
				}
				if (matrix[i][j] == 1){
					int count = 0;
					System.out.printf("Traverse started (i,j): %d, %d\n", i, j);
					count = traverse(i, j, matrix, searched, count);
					System.out.printf("Traverse ended with count %d\n", count);
					found.add(count);
				}
			}
		}
		System.out.println(found);
		return found;
  }
	
	public static int traverse(int irow, int icol, int[][] matrix, int[][] searched, int count){
		// Given the row and col index, traverse out by calling this function again
		// Mark current tile as searched
		// If current tile is a 1, +=1 to the count and return the sum of the expanded traversed tiles
		// If current tile is not a 1, return zero count
		Integer height = matrix.length;
		Integer width = matrix[0].length;
		
		if (searched[irow][icol] == 1){
			return 0;
		}
		System.out.print("Searching: ");
		System.out.printf("row: %s, ", irow);
		System.out.println(icol);
		
		searched[irow][icol] = 1;
		
		if (matrix[irow][icol] == 0){
			return 0;
		}
		if (matrix[irow][icol] == 1){
			Integer sum = 1;
			
			if (irow >= 1){
				sum = sum + traverse(irow - 1, icol, matrix, searched, count);
			}
			if (irow < height - 1){
				sum = sum + traverse(irow + 1, icol, matrix, searched, count);
			}
			if (icol >= 1){
				sum = sum + traverse(irow, icol - 1, matrix, searched, count);
			}
			if (icol < width - 1){
				sum = sum + traverse(irow, icol + 1, matrix, searched, count);
			}
			
			return sum;
		}
		return 0;
	}
}

