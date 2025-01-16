import math as m
import statistics as s

numbers = input("Enter numbers separated by a comma: ")
numbers = numbers.split(',')
for number in numbers:
    number = int(number)

minimum = min(numbers)
maximum = max(numbers)

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")

numbers2 = [int(i) for i in numbers]
mean = s.mean(numbers2)
median = s.median(numbers2)
mode = s.mode(numbers2)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")