#### for loops

### get average of student heights
student_heights = [1.72, 1.8, 2.0, 1.65, 1.78, 1.82, 1.50, 1.87, 1.77]
height = 0

for student in student_heights:
    height += student

print(f"average height in class is: {height / len(student_heights)}")

### get high_score
student_scores = [70, 90, 89, 22, 23, 35, 76, 99, 89, 12]
highest = 0

for score in student_scores:
    if highest < score:
        highest = score


print(f"High score in class: {highest}")


### add up all numbers from 1 to 1000
total = 0
for num in range(1, 101):
    total += num
print(total)


#### add up all even and odd numbers separately from 1 to 100
even = 0
odd = 0
for num in range(1, 101):
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(even, odd)


### FizzBuzz
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)