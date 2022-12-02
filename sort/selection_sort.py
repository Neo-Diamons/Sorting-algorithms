from .package import swap


def selection_sort(int_array: list[int]) -> None:
	for i in range(1, len(int_array)):
		min_index = i
		for j in range(i, len(int_array)):
			if int_array[j] < int_array[min_index]:
				min_index = j
		swap(int_array, i, min_index)
