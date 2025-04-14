'''
The setup.py file is an essential part of packaging and distributing python projects.
It is used by setuptools (or distutils in older Python versions) to define the configuration
of our project, such as its metadata, dependencies, and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Readlines from the file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                # ignore emptry line and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name='NetworkSecurity',
    version="1.0.0",
    author='Pradnyesh',
    author_email='pradnyesh2@gmail.com',
    packages=find_packages(),
    requires=get_requirements(), 
)

