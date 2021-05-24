# Unlimited positional arguments
def add(*args):
    return sum(args)


sum1 = add(1, 2, 3, 4, 5)
print(sum1)

# Unlimited named arguments (many keyword arguments)
def calculate(**kwargs):
    print(kwargs)



calculate(add=3, multiply=5)