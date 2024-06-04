import pprint
import sys

# if we can't import our upper module
sys.path.append(
    r"C:\Users\rodbe\PycharmProjects\Kind_python\modules\importing_your_own_modules") # raw-string

import my_module


my_module.floor(1)
print(my_module.NAME)
# pprint.pprint(locals())
print(my_module.ceil(7.6))

# pprint.pprint(dir(my_module))
# pprint.pprint(sys.path)  # list of paths where python looks for modules

"""
import executes only one time in the simple case
"""

print(my_module.__name__) # my_module, not __main__

import importlib

importlib.reload(my_module) # we import our import one more time