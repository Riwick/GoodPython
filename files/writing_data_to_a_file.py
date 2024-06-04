import pickle
import sys

"""
r - read
w - write (delete old data and write new)
a - append (add new data to the old one)
wb - binary
"""


def write_to_file():
    try:
        with open(f"{sys.path[0]}\\out.txt", "w") as file:
            file.write("Hello world!")
            file.write("Hello world! 2")
            file.write("Hello world! 3")
            # print(file.readlines()) - error
    except Exception as e:
        print(e)
        print("File error")


def read_from_file():
    with open(f"{sys.path[0]}\\out.txt", "r") as file:
        print(file.readlines())


def append_to_file():
    with open(f"{sys.path[0]}\\out.txt", "a") as file:
        try:
            file.write("Hello world!")
            file.write("Hello world! 2")
            file.write("Hello world! 3")
            # print(file.readlines()) - error
        except Exception as e:
            print(e)
            print("File error")


def append_to_file_with_read():
    with open(f"{sys.path[0]}\\out.txt", "a+") as file:
        try:
            file.write("Hello world! \n")
            file.write("Hello world! 2 \n")
            file.write("Hello world! 3 \n")
            file.seek(0)
            file.write("Hello world! 4\n") # write add text to the end of file
            file.writelines(["Hello world! 5\n", "Hello world! 6\n"]) # write several line to a file
            print(file.readlines())
        except Exception as e:
            print(e)
            print("File error")


def write_to_file_binary():
    with open(f"{sys.path[0]}\\out.txt", "wb") as file:
        try:
            pickle.dump("some text", file) # binary

        except Exception as e:
            print(e)
            print("File error")


def write_several_objs_to_file_binary():
     with open(f"{sys.path[0]}\\out.txt", "wb") as file:
        try:
            pickle.dump("some text 1", file) # binary
            pickle.dump("some text 2", file)
            pickle.dump("some text 3", file)

        except Exception as e:
            print(e)
            print("File error")


def read_from_file_binary():
    with open(f"{sys.path[0]}\\out.txt", "rb") as file:
        try:
            bs1 = pickle.load(file)
            bs2 = pickle.load(file)
            bs3 = pickle.load(file)
            print(bs1, bs2, bs3)
        except Exception as e:
            print(e)
            print("File error")


if __name__ == "__main__":
    pass