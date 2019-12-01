// Interesting things learned
// warning type things are hard errors, e.g. import not used


package program

func GetNthFib(n int) int {
	if n <= 1 {
		return 0
	}
	if n == 2 || n == 3 {
		return 1
	}
	
	return GetNthFib(n-1) + GetNthFib(n-2)
}

