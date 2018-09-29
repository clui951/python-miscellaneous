def bisect(arr, x):
	if len(arr) == 0:
		return 0
	if len(arr) == 1:
		if x < arr[0]:
			return 0
		if x >= arr[0]:
			return 1

	low = 0
	high = len(arr) - 1

	while low != high:
		mid = (low + high) // 2
		if x < arr[mid]:
			high = mid
		elif x == arr[mid]:
			return mid
		else: # x > arr[mid]
			if low == mid:
				low = mid + 1
			else:
				low = mid

	if low == len(arr) - 1:
		if x > arr[-1]:
			return len(arr)
	return low # or high, the same


if __name__ == "__main__":
	print("=== bisect ===")

	assert bisect([], 1) == 0
	assert bisect([], 10) == 0
	assert bisect([5], 1) == 0
	assert bisect([5], 10) == 1

	assert bisect([2, 4], 1) == 0
	assert bisect([2, 4], 2) == 0
	assert bisect([2, 4], 3) == 1
	assert bisect([2, 4], 4) == 1
	assert bisect([2, 4], 5) == 2
	
	assert bisect([2, 4, 6], 1) == 0
	assert bisect([2, 4, 6], 2) == 0
	assert bisect([2, 4, 6], 3) == 1
	assert bisect([2, 4, 6], 4) == 1
	assert bisect([2, 4, 6], 5) == 2
	assert bisect([2, 4, 6], 6) == 2
	assert bisect([2, 4, 6], 7) == 3

	assert bisect([2, 4, 6, 9], 1) == 0
	assert bisect([2, 4, 6, 9], 2) == 0
	assert bisect([2, 4, 6, 9], 3) == 1
	assert bisect([2, 4, 6, 9], 4) == 1
	assert bisect([2, 4, 6, 9], 5) == 2
	assert bisect([2, 4, 6, 9], 6) == 2
	assert bisect([2, 4, 6, 9], 7) == 3
	assert bisect([2, 4, 6, 9], 8) == 3
	assert bisect([2, 4, 6, 9], 9) == 3
	assert bisect([2, 4, 6, 9], 10) == 4

	assert bisect([2, 4, 6, 9, 10], 1) == 0
	assert bisect([2, 4, 6, 9, 10], 2) == 0
	assert bisect([2, 4, 6, 9, 10], 3) == 1
	assert bisect([2, 4, 6, 9, 10], 4) == 1
	assert bisect([2, 4, 6, 9, 10], 5) == 2
	assert bisect([2, 4, 6, 9, 10], 6) == 2
	assert bisect([2, 4, 6, 9, 10], 7) == 3
	assert bisect([2, 4, 6, 9, 10], 8) == 3
	assert bisect([2, 4, 6, 9, 10], 9) == 3
	assert bisect([2, 4, 6, 9, 10], 10) == 4
	assert bisect([2, 4, 6, 9, 10], 11) == 5

	print("=== done! ===")