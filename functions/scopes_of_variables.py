N = 100  # file namespace (global)


def my_func():
    lst = []  # function namespace (local)
    x = 1


# print(lst) - error, because lst in local namespace
print(N)


def my_func2():
    lst = []  # function namespace (local)
    x = 1
    print(N)


my_func2()  # success, because variable N is in global namespace


def my_func3():
    # this variable is local, although we have N in global namespace
    # (we have created a new variable)
    N = 20
    lst = []  # function namespace (local)
    x = 1
    print(N)


my_func3()
print(N)


def my_func4():
    global N  # this N is global
    N = 20
    lst = []  # function namespace (local)
    x = 1
    print(N)  # 20


my_func4()
print(N)


def my_func5():
    N = 231
    # global N - error, because N is local
    lst = []  # function namespace (local)
    x = 1
    print(N)  # 231


my_func5()
print(N)


x = 0


def outer():  # type: ignore
    x = 1

    def inner():
        x = 2
        print(f"inner {x=}")

    inner()
    print(f"outer {x=}")


outer()
print(f"global {x=}")

# global > outer > inner

print()

x = 0


def outer(): # type: ignore
    x = 1

    def inner():
        nonlocal x  # x from outer function
        x = 2
        print(f"inner {x=}")

    inner()
    print(f"outer {x=}")


outer()
print(f"global {x=}")

# we can use nonlocal only in 2 locals namespaces

print()

x = 0


def outer():
    global x
    x += 1
    
    def inner():
        # nonlocal x - error, because x in global namespace
        x = 2
        print(f"inner {x=}")

    inner()
    print(f"outer {x=}")


outer()
print(f"global {x=}")
