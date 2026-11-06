from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->list[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        
        requirements = [req for req in requirements if req and not req.startswith('-e .')]
    
    return requirements

setup(
    name='ml_course',
    version='0.1.0',
    author='Gebrekidan Gebremedhin',
    email='gebrekidan.gebremedhin@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)