numbers = [1, -2, 3, -4, 5, -6, 8]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]

print(even_nums)