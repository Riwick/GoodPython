from functools import wraps
import math


def df_decorator(dx):
    def func_decorator(func):
        @wraps(func)  # save decorated func name and docstring
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) -
                   func(x, *args, **kwargs)) / dx
            return res

        # wrapper.__name__ = func.__name__ # save decorated func name
        # wrapper.__doc__ = func.__doc__ # save decorated func docstring

        return wrapper
    return func_decorator


@df_decorator(dx=0.00001)
def sin_df(x):
    """_summary_

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    return math.sin(x)

print(sin_df.__name__)
print(sin_df.__doc__)

df = sin_df(math.pi / 3)
print(df)


# f = df_decorator(dx=0.0001)
# sin_df = f(sin_df)  # f = df_decorator(dx=0.0001)(sin_df)
# print(sin_df(math.pi / 3))
