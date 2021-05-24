# Unlimited positional arguments
def add(*args):
    return sum(args)


sum1 = add(1, 2, 3, 4, 5)
print(sum1)

# Unlimited named arguments (many keyword arguments)
def calculate(n, **kwargs):
    # for (k, v) in kwargs.items():
    #     print(k)
    #     print(v)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


kwarg1 = calculate(2, add=3, multiply=5)
print(kwarg1)