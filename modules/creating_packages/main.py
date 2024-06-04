import package

print(dir(package))
print(package.get_python())
print(package.get_java())

# print(package.P_NAME) - error because P_NAME not in __all__ list in python.py

print(package.java_doc.j_doc)
print(package.python_doc.p_doc)