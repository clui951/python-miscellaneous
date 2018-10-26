# permutations are generated recursively
# for every element in the input, place it at the beginning and append to the permutations of the rest of the elements
# at every level, use yield (generators) to return, to not have to build up O(n!) memory
# memory is O(n), call stack
def permutations(input):
	count = 0
	for p in permutations_internal(input):
		count += 1
		print(count, p)

def permutations_internal(input):
	if len(input) == 0:
		yield ""
	elif len(input) == 1:
		yield input
	elif len(input) == 2:
		yield input
		yield input[::-1]
	else:
		for i in range(len(input)):
			# for generator, you cannot just do str + generator directly; must iterate or set to variable
			for pp in permutations_internal(input[:i] + input[i+1:]):
				yield input[i] + str(pp)

# RETURNING FULL LIST, MEMORY MUST BE O(# perms)
# for every character
# for each element in list so far, 
#	create a new element by sticking character in every possible location (include the very end)
# 	replace the running list with the current list generated after sticking in characters
def permutations2(nums):
	result_list = [[]]
	for n in nums:
		new_result_list = []
		for res in result_list:
			for i in range(len(res) + 1):
				current_perm = res[:i] + [n] + res[i:]
				new_result_list.append(current_perm)
		result_list = new_result_list
	
	count = 0
	for p in result_list:
		count += 1
		print(count, "".join(p))

	return result_list

# PRINTING ALL ELEMENTS, MEMORY CAN BE LINEAR TO LENGTH IF DONE IN PLACE
# done in place by nested function and swapping/backtracking
# does not have to hold in memory all combinations previous
def permutations3(nums):
	count = 0
	tracker = list(nums)
	
	def perm(nums, i):
		nonlocal count 

		if i == len(nums):
			count += 1
			print(count, "".join(tracker))
			return
		for j in range(i, len(nums)):
			tracker[i], tracker[j] = tracker[j], tracker[i]
			perm(nums, i + 1)
			# backtracking
			tracker[i], tracker[j] = tracker[j], tracker[i]

	perm(nums, 0)


	

if __name__ == "__main__":
	print("=== permutations ===")

	# permutations("")
	# print("--")
	# permutations("1")
	# print("--")
	# permutations("12")
	# print("--")
	# permutations("123")
	print("--")
	permutations("1234")
	print("--")
	permutations2("1234")
	print("--")
	permutations3("1234")
	# print("--")
	# permutations("12345")
	# print("--")
	# permutations("12234")
	# print("--")
	# permutations("12333455")

	print("=== done! ===")