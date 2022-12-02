def merge_array(
		int_array: list[int], left: list[int], right: list[int]) -> None:
	i = j = k = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			int_array[k] = left[i]
			i += 1
		else:
			int_array[k] = right[j]
			j += 1
		k += 1

	for i in range(i, len(left)):
		int_array[k] = left[i]
		k += 1
	for j in range(j, len(right)):
		int_array[k] = right[j]
		k += 1


def merge_sort(int_array: list[int]) -> None:
	if 1 < len(int_array):
		mid = len(int_array) // 2
		left = int_array[:mid]
		right = int_array[mid:]
		merge_sort(left)
		merge_sort(right)
		merge_array(int_array, left, right)
