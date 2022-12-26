##This file is required in every python project & is mainly required to create Python packages
from setuptools import find_packages,setup
from typing import List

requirement_file = "/config/workspace/requirements.txt"

hyphen_e = "-e ."

def get_requirements()->List[str]:
    with open(requirement_file) as var:
        requirement_list = var.readlines()
        requirement_list = [i.replace("\n","").strip() for i in requirement_list if i != hyphen_e]
    return requirement_list



#find_packages() is a function from the setuptools library in Python that is used to find all 
# Python packages in a specified directory. 
# It is commonly used in the setup.py script of a Python project to automatically discover all of the packages 
# that should be included in the project when it is installed

#When this script is run, find_packages() will search the current directory (and any subdirectories) for directories that 
#contain a __init__.py file. These directories are considered to be Python packages, 
#and they will be included in the list of packages that is passed to the setup() function.
setup(
    name = "sensor",
    version = "0.0.1",
    author = "Kartikeya",
    author_email = "kartikeyasharma40@gmail.com",
    packages = find_packages(), #This searches directories for __init__.py file and creates packages
    install_requires = get_requirements(), # The install_requires argument in a Python project's setup.py script specifies a list 
    #of dependencies that should be installed along with the project when it is installed.
)
