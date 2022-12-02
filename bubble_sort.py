def swap(int_array: list[int], i: int) -> int:
	if int_array[i + 1] < int_array[i]:
		tmp = int_array[i]
		int_array[i] = int_array[i + 1]
		int_array[i + 1] = tmp
		return 1
	return 0


def bubble_sort(int_array: list[int]) -> None:
	error = 1
	while error != 0:
		error = 0
		for i in range(len(int_array) - 1):
			error += swap(int_array, i)
