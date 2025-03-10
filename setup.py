## To build entire machine learning project as a package 
from setuptools import find_packages,setup## automatically find out all the packages that are present in entire machine learning application or directory 

HYPEN_E_DOT='-e .' ## If we run direct setup then no need of .e in requiement as it will again run setup.py and loop will create
from typing import List
def get_requirements(file_path:str) ->List[str]:##reads a file (typically requirements.txt) and returns(->) a list of non-empty, non-commented package names.
    '''
    this function will return the list of requirements
    '''
    requirements=[] ## makeing as a empty list 
    with open(file_path) as file_obj: ## open and create as tem file object 
        requirements=file_obj.readlines() ## one one element will be read 
        requirements=[req. replace("\n","") for req in requirements] ## problem wne we go to next line/n will added to remove this replace with blank

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) 

setup(
name='mlproject',
version='0.0.1',
author='Sanjay',
author_email='sanjayahirwar1323@gmail.com',
packages=find_packages(), ## when findpackages running it will see in how many you have__init__.py then it will directly consider this sourse or folder or src as package itself
install_requires=get_requirements('requirements.txt') 
)