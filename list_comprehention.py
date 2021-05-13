numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_num = [num**2 for num in numbers]
print(squared_num)
even_num = [num for num in numbers if num % 2 == 0]
print(even_num)
with open("file1.txt") as file:
    file1 = file.readlines()
with open("file2.txt") as file:
    file2 = file.readlines()
result = [int(num.strip()) for num in file1 if num in file2]
print(result)