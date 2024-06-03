def recursion(value):
    print(value)
    if value < 4:
        recursion(value + 1)
    print(value)


recursion(1)

print()


def factorial(n):
    # n * (n - 1) * (n - 2) * ... * 1
    if n <= 0:
        return 1
    return n * factorial(n - 1)


print(factorial(6))

# Example

F = {
    "C:": {
        "Python39": ["python.exe", "python.ini"],
        "Program Files": {
            "Java": ["README.txt", "Welcome.html", "java.exe"],
            "MATLAB": ["matlab.bat", "matlab.exe", "mcc.bar"]
        },
        "Windows": {
            "System32": ["acledit.dll", "aclui.dll", "zipfldr.dll"]
        }
    }
}


def get_files(path, depth=0):
    for f in path:
        print(" "*depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth + 2)
        else:
            for file in path[f]:
                print(" "*(depth + 2) + file)


get_files(F)

"""
recursive functions are great for sorting through values in a fractal structure
"""
