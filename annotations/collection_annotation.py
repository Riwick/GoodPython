from typing import List, Tuple, Dict, Set, Union, Optional, Any, Callable

lst: list = [1, 2, 3]

lst_2: list[int] = [1, "2", 3]  # only ints in list

# for python < 3.9
lst_3: List[int] = [1, "2", 3]


# there should be 2 elements of type int and str
addr: tuple[int, str] = (1, "2")

# there should be 3 elements of type str, str and int
book: tuple[str, str, int]
book = ("123", "123", 123)

elems: tuple[float, ...] = (1.2, 23.2, 123)  # tuple of floats

# for python < 3.9
addr_2: Tuple[int, str] = (123, "232")


# dict with str keys and int values
words: dict[str, int] = {"one": 1, "two": 2}

# for python < 3.9
words_2: Dict[str, int] = {"one": 1, "two": 2}

# set with str elements
persons: set[str] = {"123", "323"}
# for python < 3.9
persons_2: Set[str] = {"123", "323", 233}


Digits = Union[int, float]  # int or float


def get_positive(digits: Optional[list[Digits]] = None) -> Any:
    # digits are list[int, float] or None
    if digits:
        return list(filter(lambda x: x > 0, digits))
    return []


print(get_positive([1, -2, 3123, 32, 2, True]))
print(get_positive([1, -2, 3123, 32, 2, 3.3]))


# Callable[[TypeArg1, TypeArg2, ...], ReturnType] - type for callable objects

def hello_callable():
    # Callable[None, None]
    print("Hello callable")


def even(x: int):
    return x % 2 == 0


def get_filtered_list(flt: Callable[[int], bool], lst: list[int] = None) -> list[int]:
    # flt is func, where args are int, returns bool, lst is a list of ints - default None
    if lst is None:
        return []
    return list(filter(flt, lst))


print(get_filtered_list(even, [i for i in range(1, 11)]))
