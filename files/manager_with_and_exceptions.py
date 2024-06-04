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


print()
# block with


try:
    # manager with automatically close the file
    with open(f"{sys.path[0]}\\file.txt", encoding="utf-8") as file:
        print(file.readlines())

except FileNotFoundError:  # catch only one exception
    print("unable to open file")
except:  # catch all exceptions
    print("Catch any exceptions")

finally:
    print(file.closed)
