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


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car1 = Car(make="Nissan", model="GT-R")
print(my_car1.make, my_car1.model)

my_car2 = Car(make="Nissan")
print(my_car2.make, my_car2.model)