def swap(int_array: list[int], a: int, b: int) -> None:
	tmp = int_array[a]
	int_array[a] = int_array[b]
	int_array[b] = tmp
