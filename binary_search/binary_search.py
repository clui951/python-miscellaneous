# set up base cases len 0/1
# continue searching while low/high pointers not equal and pointing to search range
# find the mid point and compare search element to mid element
#  	if val < mid, search lower half
# 	if val == mid, return mid index
# 	if val > mid,
#		if low == mid, check element right above low; return that index if found, or None
#		else, search upper half
# element not found if low is equal high
def binary_search(arr, val):
	if len(arr) == 0:
		return None
	if len(arr) == 1:
		if arr[0] == val:
			return 0
		else:
			return None

	low = 0
	high = len(arr) - 1
	while low != high:
		mid = (low + high) // 2
		if val < arr[mid]:
			high = mid
		elif val == arr[mid]:
			return mid
		else:
			if low == mid:
				if arr[low + 1] == val:
					return low + 1
				else:
					return None
			else:
				low = mid
	return None

if __name__ == "__main__":
	print("=== binary_search ===")

	assert binary_search([], 1) == None

	assert binary_search([5], 1) == None
	assert binary_search([5], 10) == None
	assert binary_search([5], 5) == 0

	assert binary_search([2, 4], 1) == None
	assert binary_search([2, 4], 2) == 0
	assert binary_search([2, 4], 3) == None
	assert binary_search([2, 4], 4) == 1
	assert binary_search([2, 4], 5) == None
	
	assert binary_search([2, 4, 6], 1) == None
	assert binary_search([2, 4, 6], 2) == 0
	assert binary_search([2, 4, 6], 3) == None
	assert binary_search([2, 4, 6], 4) == 1
	assert binary_search([2, 4, 6], 5) == None
	assert binary_search([2, 4, 6], 6) == 2
	assert binary_search([2, 4, 6], 7) == None

	assert binary_search([2, 4, 6, 9], 1) == None
	assert binary_search([2, 4, 6, 9], 2) == 0
	assert binary_search([2, 4, 6, 9], 3) == None
	assert binary_search([2, 4, 6, 9], 4) == 1
	assert binary_search([2, 4, 6, 9], 5) == None
	assert binary_search([2, 4, 6, 9], 6) == 2
	assert binary_search([2, 4, 6, 9], 7) == None
	assert binary_search([2, 4, 6, 9], 8) == None
	assert binary_search([2, 4, 6, 9], 9) == 3
	assert binary_search([2, 4, 6, 9], 10) == None

	assert binary_search([2, 4, 6, 9, 10], 1) == None
	assert binary_search([2, 4, 6, 9, 10], 2) == 0
	assert binary_search([2, 4, 6, 9, 10], 3) == None
	assert binary_search([2, 4, 6, 9, 10], 4) == 1
	assert binary_search([2, 4, 6, 9, 10], 5) == None
	assert binary_search([2, 4, 6, 9, 10], 6) == 2
	assert binary_search([2, 4, 6, 9, 10], 7) == None
	assert binary_search([2, 4, 6, 9, 10], 8) == None
	assert binary_search([2, 4, 6, 9, 10], 9) == 3
	assert binary_search([2, 4, 6, 9, 10], 10) == 4
	assert binary_search([2, 4, 6, 9, 10], 11) == None

	print("=== done! ===")