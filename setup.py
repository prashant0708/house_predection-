from setuptools import setup 
from typing import List

#Declaring variables for setup function
Project_Name="Housing-Predictor"
Version="0.0.1"
AUTHOR= "Prashant_Kumar_Singh"
Description="This is my first CICD based Project"
Packages=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description:This function is going to return list of requirements 
    mention in requirements.txt file 
    return This function is going to return a list which contain name of libraries
    mentoned in requirements.txt file 

    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readline()

setup(
name=Project_Name,
version=Version,
author=AUTHOR,
description=Description,
packages=Packages,
install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())