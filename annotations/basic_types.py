from typing import Union, Optional, Any, Final

cnt: int = 0  # int
msg: str = "hello"  # str
lst = [1, 2, 3]  # list

cnt = -5.3  # it's not an error
msg = 0  # it's just warning

"""
Type annotations make it easier to write code and are only needed by programmers
"""


def show_methods(x):
    print(x)  # we don't have any clues without annotation


def show_methods2(x: str):
    print(x)  # we have some hints with annotation


def default_value(x: int = 1):  # we set default value to x
    print(x)


default_value()  # we print our default value
default_value(123)


# if the function does not have a return, then it returns None
def print_something() -> None:
    print("Something")


print_something()


# The function can also return a specific type of data
def return_something(x: float, y: float) -> float:
    return x + y


print(return_something(1.2, 2.2))


# module typing
MAX_VALUE: Final = 1000  # constant value

digit = Union[int, float]  # int or float
not_opt_str = Union[str, None]  # int or None
opt_str = Optional[str]  # str or None

# Union[str, None] == Optional[str]


MAX_VALUE = 1232  # now we have a warning


# x: float or int or str, return float or None
def mul2(x: float | int | str, y: digit) -> Optional[float]:
    return x + y


# x: any type of data, return any type of data
def show_x(x: Any, descr: Optional[str] = None) -> Any:
    if descr:
        print(f"{descr}: {x}")
    else:
        print(f"x = {x}")


show_x(55.21313)


print(mul2(2, 4))
print(mul2.__annotations__)  # all annotations in function
