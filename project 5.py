import random   
from random import shuffle

nums = [45, 54, 64, 34, 57, 78, 43, 65, 89, 44]
high_num = 0

for num in nums:
    if num > high_num:
        high_num = num
print(f"highest num is: {high_num}")

# total = 0
# for n in range(1,101):
#     total += n
# print(total )

sum_of_even = 0
for n in range(2, 101, 2):
    sum_of_even += n

print(sum_of_even)
print(sum(range(2, 101, 2)))


# fizzbuzz

def dev_by_3(num):
    if num % 3 == 0:
        return True


def dev_by_5(num):
    if num % 5 == 0:
        return True


def dev_by_3_and_5(num):
    if dev_by_3(num) and dev_by_5(num):
        return True


for n in range(1, 101):
    if dev_by_3_and_5(n):
        print("fizzbuzz")
    elif dev_by_5(n):
        print("buzz")
    elif dev_by_3(n):
        print("fizz")
    else:
        print(n)

# password generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

rand_letters = random.sample(letters, nr_letters)
rand_numbers = random.sample(numbers, nr_numbers)
rand_symbols = random.sample(symbols, nr_symbols)

password = [*rand_letters, *rand_numbers, *rand_symbols]
shuffle(password)
sep = ""
print("Your random password is: ", sep.join(password))
