def binary_search(A, x, strong_search):
	low = 0
	high = len(A)  - 1
	while low <= high:
		mid = (low + high) // 2
		if A[mid] == x:
			return mid
		elif A[mid] > x:
			high = mid - 1
		else:
			low = mid + 1
	if strong_search:
		return -1
	else:
		return mid