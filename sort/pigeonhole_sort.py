# Only work for list of int with unique value

def pigeonhole_sort(int_array: list[int]) -> None:
	min_val = min(int_array)
	index_array = [None] * (max(int_array) - min_val + 1)

	for i in range(len(int_array)):
		index_array[int_array[i] - min_val] = int_array[i]

	i = 0
	for j in range(len(index_array)):
		if index_array[j] is not None:
			int_array[i] = index_array[j]
			i += 1
