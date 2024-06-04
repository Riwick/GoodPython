from math import *  # type: ignore # we import all objects from math without link
from math import ceil as cl
from math import ceil, e  # type: ignore # we import only 2 objects
from math import sin  # we import only one function
from math import pi  # we import only one variable
import math as mt  # link to math namespace
import time  # link to time namespace
import pprint  # link to pprint namespace

# math, time, pprint are standard modules

"""
all imports should be in the first lines of program
"""

math = "math"
# pprint.pprint(locals())
a = mt.ceil(1.8)
print(a)
print(mt.pi)


print(pi)

print(sin(.8))

print(ceil(2.3), e)


def ceil(x):  # we rewrite ceil function from math
    print("It\'s local ceil function")


print(ceil(1.5))


print(cl(4.5))

pprint.pprint(locals())
