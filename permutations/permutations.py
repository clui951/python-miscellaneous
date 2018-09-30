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

	

if __name__ == "__main__":
	print("=== permutations ===")

	permutations("")
	print("--")
	permutations("1")
	print("--")
	permutations("12")
	print("--")
	permutations("123")
	print("--")
	permutations("1234")
	# print("--")
	# permutations("12345")
	print("--")
	permutations("12234")
	# print("--")
	# permutations("12333455")

	print("=== done! ===")