def swap(int_array: list[int], a: int, b: int) -> None:
	tmp = int_array[a]
	int_array[a] = int_array[b]
	int_array[b] = tmp


def selection_sort(int_array: list[int]) -> None:
	for i in range(1, len(int_array)):
		min_index = i
		for j in range(i, len(int_array)):
			if int_array[j] < int_array[min_index]:
				min_index = j
		swap(int_array, i, min_index)
