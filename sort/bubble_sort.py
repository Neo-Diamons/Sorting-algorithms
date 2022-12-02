from .package import swap


def bubble_sort(int_array: list[int]) -> None:
	error = 1
	while error != 0:
		error = 0
		for i in range(len(int_array) - 1):
			if int_array[i + 1] < int_array[i]:
				swap(int_array, i, i + 1)
				error += 1
