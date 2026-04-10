from setuptools import find_packages, setup
from typing import List

hyphen = "-e ."

def get_requirements(file_id:str)->list[str]:   # -> list[str] → The return type annotation. It indicates the function will return a list of strings.
    with open(file_id) as f:
        requirements = f.read().splitlines()

# "-e ." automatically triggers this setup file

    if hyphen in requirements:
        requirements.remove(hyphen)
    return requirements


setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A short description of the project.',
    author='Yash',
    install_requires=get_requirements('requirements.txt'),
)