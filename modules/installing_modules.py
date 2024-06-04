# pip list - shows all of your installed packages
"""
for python3.9

Package    Version
---------- -------
pip        23.2.1
setuptools 68.2.0
wheel      0.41.2
"""


# pip install <package_name>

# pip install numpy
"""
Package    Version
---------- -------
numpy      1.26.4 - we just installed the package
pip        23.2.1
setuptools 68.2.0
wheel      0.41.2
"""

# pip install <package_name>==<version>


#pip install sqlalchemy==1.0
"""
Package    Version
---------- -------
numpy      1.26.4
pip        23.2.1
setuptools 68.2.0
SQLAlchemy 1.0.0 - we just installed the package with specific version
wheel      0.41.2
"""

# https://pypi.org/ - a website with all packages for python

"""
Some packages are linked to a specific version of python
"""


# pip freeze > requirements.txt - we save all our packages in one file

# pip install -r requirements.txt - we install all packages from one file