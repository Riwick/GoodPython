"""
try:
    <operator>
except <Exception>: - execute if block try will raise exception
    <operator>
else: - execute if block finally was not called
    <operator>
finally: - execute in any case
    <operator>
"""


import sys


try:
    # a = 1/0
    a = []
    print(a[123])
    while True:
        pass

except KeyboardInterrupt:  # press Ctrl + C
    print("shutdown script")
    exit()

except ZeroDivisionError:
    print("You can't devide by zero")

except Exception:
    print("Something has gone wrong!")


try:
    file = open(f"{sys.path[0]}\\file.txt", encoding="utf-8")

    try:
        s = file.readlines()
        print(s)

    finally:
        file.close()
        print(file.closed)

except FileNotFoundError:  # catch only one exception
    print("unable to open file")
except:  # catch all exceptions
    print("Catch any exceptions")

else:
    print("this code will be executed if the finally block is not executed")

finally:
    print("this code will be executed anyway")


# Exception is a basic exception class


def some_func(a=None, b=None):
    assert a or b, "You need to write at least one argument"  # custom error message


some_func(1)


class Something:
    def do_some(self):
        raise NotImplementedError  # raise exception in function


# s = Something()
# s.do_some()


class CustomException(Exception):  # create your own exception
    ...  # pass


def some_func1(name):
    if len(name) < 5:
        raise CustomException("Name is too short")


# some_func1("Anna")


try:
    z = 1/0
except ZeroDivisionError as e:
    print(e)  # print exception description


# def main():
#     try:
#         f1()
#     except SomeError:
#         print("Some error")
#         raise - throw exception up
#     try:
#         f2()
#     except SomeError2:
#         pass


# if __name__ == "__main__":
#     try:
#         main()
#     except Exception:
#         print(...)
#         main(...)


# it is better to use the if - else block than exceptions
# exceptions should be called infrequently
