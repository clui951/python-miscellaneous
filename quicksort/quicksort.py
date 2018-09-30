import itertools 

# quicksort array in place, with low/high pointers specifying range to sort
# for every call, if low < high ptr, partition the array
# partition takes the last element in range as pivot
# 	i is the pointer for last element that is lower than the pivot; starts below low ptr
#	iterate pointer j from low ptr to just before high ptr
# 	if element j < pivot, increment i to next spot (start of elements that are >= pivot), and swap elements j & i
# 	as a result, i again points to the last element < pivot
# 	at the very end of partition, swap the pivot and the first element of the >= pivot section
# 	return the index of pivot
# quicksort uses the pivot to divide & conquer recursively
def quicksort(arr, low, high):
	if low < high:
		part = partition(arr, low, high)

		quicksort(arr, low, part - 1)
		quicksort(arr, part+1, high)
	return arr

def partition(arr, low, high):
	partition_val = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] < partition_val:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1
	

if __name__ == "__main__":
	print("=== quicksort ===")

	assert quicksort([], 0, 0) == []

	assert quicksort([1], 0, 0) == [1]

	assert quicksort([1, 2], 0, 1) == [1, 2]
	assert quicksort([2, 1], 0, 1) == [1, 2]

	assert quicksort([1, 2, 3], 0, 2) == [1, 2, 3]
	assert quicksort([1, 3, 2], 0, 2) == [1, 2, 3]
	assert quicksort([2, 1, 3], 0, 2) == [1, 2, 3]
	assert quicksort([2, 3, 1], 0, 2) == [1, 2, 3]
	assert quicksort([3, 1, 2], 0, 2) == [1, 2, 3]
	assert quicksort([3, 2, 1], 0, 2) == [1, 2, 3]

	assert quicksort([1, 2, 3, 4], 0, 3) == [1, 2, 3, 4]
	assert quicksort([1, 2, 4, 3], 0, 3) == [1, 2, 3, 4]
	assert quicksort([1, 3, 2, 4], 0, 3) == [1, 2, 3, 4]
	assert quicksort([1, 3, 4, 2], 0, 3) == [1, 2, 3, 4]
	assert quicksort([1, 4, 2, 3], 0, 3) == [1, 2, 3, 4]
	assert quicksort([1, 4, 3, 2], 0, 3) == [1, 2, 3, 4]
	assert quicksort([2, 1, 3, 4], 0, 3) == [1, 2, 3, 4]
	assert quicksort([2, 1, 4, 3], 0, 3) == [1, 2, 3, 4]
	assert quicksort([2, 3, 1, 4], 0, 3) == [1, 2, 3, 4]
	assert quicksort([2, 3, 4, 1], 0, 3) == [1, 2, 3, 4]
	assert quicksort([2, 4, 1, 3], 0, 3) == [1, 2, 3, 4]
	assert quicksort([2, 4, 3, 1], 0, 3) == [1, 2, 3, 4]
	assert quicksort([3, 1, 2, 4], 0, 3) == [1, 2, 3, 4]
	assert quicksort([3, 1, 4, 2], 0, 3) == [1, 2, 3, 4]
	assert quicksort([3, 2, 1, 4], 0, 3) == [1, 2, 3, 4]
	assert quicksort([3, 2, 4, 1], 0, 3) == [1, 2, 3, 4]
	assert quicksort([3, 4, 1, 2], 0, 3) == [1, 2, 3, 4]
	assert quicksort([3, 4, 2, 1], 0, 3) == [1, 2, 3, 4]
	assert quicksort([4, 1, 2, 3], 0, 3) == [1, 2, 3, 4]
	assert quicksort([4, 1, 3, 2], 0, 3) == [1, 2, 3, 4]
	assert quicksort([4, 2, 1, 3], 0, 3) == [1, 2, 3, 4]
	assert quicksort([4, 2, 3, 1], 0, 3) == [1, 2, 3, 4]
	assert quicksort([4, 3, 1, 2], 0, 3) == [1, 2, 3, 4]
	assert quicksort([4, 3, 2, 1], 0, 3) == [1, 2, 3, 4]

	assert quicksort([1, 2, 3, 4, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 2, 3, 5, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 2, 4, 3, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 2, 4, 5, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 2, 5, 3, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 2, 5, 4, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 3, 2, 4, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 3, 2, 5, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 3, 4, 2, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 3, 4, 5, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 3, 5, 2, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 3, 5, 4, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 4, 2, 3, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 4, 2, 5, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 4, 3, 2, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 4, 3, 5, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 4, 5, 2, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 4, 5, 3, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 5, 2, 3, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 5, 2, 4, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 5, 3, 2, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 5, 3, 4, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 5, 4, 2, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([1, 5, 4, 3, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 1, 3, 4, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 1, 3, 5, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 1, 4, 3, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 1, 4, 5, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 1, 5, 3, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 1, 5, 4, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 3, 1, 4, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 3, 1, 5, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 3, 4, 1, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 3, 4, 5, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 3, 5, 1, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 3, 5, 4, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 4, 1, 3, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 4, 1, 5, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 4, 3, 1, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 4, 3, 5, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 4, 5, 1, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 4, 5, 3, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 5, 1, 3, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 5, 1, 4, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 5, 3, 1, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 5, 3, 4, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 5, 4, 1, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([2, 5, 4, 3, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 1, 2, 4, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 1, 2, 5, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 1, 4, 2, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 1, 4, 5, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 1, 5, 2, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 1, 5, 4, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 2, 1, 4, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 2, 1, 5, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 2, 4, 1, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 2, 4, 5, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 2, 5, 1, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 2, 5, 4, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 4, 1, 2, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 4, 1, 5, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 4, 2, 1, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 4, 2, 5, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 4, 5, 1, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 4, 5, 2, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 5, 1, 2, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 5, 1, 4, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 5, 2, 1, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 5, 2, 4, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 5, 4, 1, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([3, 5, 4, 2, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 1, 2, 3, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 1, 2, 5, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 1, 3, 2, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 1, 3, 5, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 1, 5, 2, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 1, 5, 3, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 2, 1, 3, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 2, 1, 5, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 2, 3, 1, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 2, 3, 5, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 2, 5, 1, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 2, 5, 3, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 3, 1, 2, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 3, 1, 5, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 3, 2, 1, 5], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 3, 2, 5, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 3, 5, 1, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 3, 5, 2, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 5, 1, 2, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 5, 1, 3, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 5, 2, 1, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 5, 2, 3, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 5, 3, 1, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([4, 5, 3, 2, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 1, 2, 3, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 1, 2, 4, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 1, 3, 2, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 1, 3, 4, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 1, 4, 2, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 1, 4, 3, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 2, 1, 3, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 2, 1, 4, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 2, 3, 1, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 2, 3, 4, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 2, 4, 1, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 2, 4, 3, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 3, 1, 2, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 3, 1, 4, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 3, 2, 1, 4], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 3, 2, 4, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 3, 4, 1, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 3, 4, 2, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 4, 1, 2, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 4, 1, 3, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 4, 2, 1, 3], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 4, 2, 3, 1], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 4, 3, 1, 2], 0, 4) == [1, 2, 3, 4, 5]
	assert quicksort([5, 4, 3, 2, 1], 0, 4) == [1, 2, 3, 4, 5]


	base = [1, 2, 3, 4]
	for perm in itertools.permutations(base):
		assert quicksort(list(perm), 0, len(base) - 1) == base

	base = [1, 2, 3, 3, 3, 4, 5, 5]
	for perm in itertools.permutations(base):
		assert list(quicksort(list(perm), 0, len(base) - 1)) == base

	print("=== done! ===")