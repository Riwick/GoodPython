# import importing_your_own_modules - error circular import
# from math import * - not recommended
from math import ceil, pi

NAME = "my_module"


def floor(x):
    print(f"floor function from my_module {x=}")


print(NAME) # when we import this module print() is running

if __name__ == "__main__": # this lines execute when we running my_module.py, not main.py
    for i in range(5):
        print(NAME)
