#with the help of this...i can build my entire machine learning project or algo as a package and even deply in python pypi

#building you application as a package itself

from setuptools import find_packages,setup
from typing import List

#this function will return the list of requirements

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements 

setup(
    name='demo',
    version='0.0.1',
    author='sumukh',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)