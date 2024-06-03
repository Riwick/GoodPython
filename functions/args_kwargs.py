m = max(1, 2, 4, -5)
print(m)


def os_path(*args, sep="\\"):
    print(args)
    path = sep.join(args)
    return path


os_path("123", "2323", "5123")
print(os_path("123", "2323", "5123", sep="__"))
print(os_path())



def os_path1(disk, *args, sep="\\", **kwargs): # formal params needs to be before **kwargs
    print(args, kwargs)

    args = (disk,) + args
    if "trim" in kwargs and kwargs["trim"]:
        args = [x.strip() for x in args]

    path = sep.join(args)

    return path


os_path1("123", "2323", "5123", sep="123", trim=True)

print(os_path1("123", "2323 ", "5123  ", trim=False))
print(os_path1("123", "2323", "5123", sep="___", trim=True))