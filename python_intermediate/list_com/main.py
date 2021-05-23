numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [i*i for i in numbers]
even_numbers = [i for i in numbers if i % 2 == 0]

print(squared_numbers)
print(even_numbers)

# Get numbers from file1 and file2 and see which contain similar numbers
with open("file1.txt") as file1:
    content1 = file1.read().splitlines()

with open("file2.txt") as file2:
    content2 = file2.read().splitlines()


# turn strings into integers in each list
content1 = [int(num) for num in content1]
content2 = [int(num) for num in content2]

common = sorted(list(set(content1) & set(content2)))

print(common)



