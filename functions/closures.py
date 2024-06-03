def say_name(name):  # type: ignore
    def say_goodbye():
        print(f"Dont say me goodbye {name}!")

    say_goodbye()


say_name("Riwi")


def say_name(name):
    def say_goodbye():
        print(f"Dont say me goodbye {name}!")

    return say_goodbye


f = say_name("Riwi")
f2 = say_name("Python")
f()
f2()


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = counter(10)
c2 = counter()

print(c1(), c2(), sep=", ")
print(c1(), c2(), sep=", ")
print(c1(), c2(), sep=", ")


def strip_str(strip_chars=" "):
    
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_str()
strip2 = strip_str(" !.,?;")
print(strip1(" hello python!.. "))
print(strip2(" hello python!.. "))
