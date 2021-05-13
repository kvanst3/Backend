import random


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_num = [num**2 for num in numbers]
print(squared_num)

even_num = [num for num in numbers if num % 2 == 0]
print(even_num)

with open("file1.txt") as file:
    file1 = file.readlines()
with open("file2.txt") as file:
    file2 = file.readlines()
result = [int(num) for num in file1 if num in file2]
print(result)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_score = {name: random.randint(0,10) for name in names}
print(student_score)

passed_students = {key: value for (key, value) in student_score.items() if value >= 6}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {i: len(i) for i in sentence.split()}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)
