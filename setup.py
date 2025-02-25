from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT= "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name ='sticker_sales_forecast',
    version ='0.0.1',
    author ='Mohammed Shifin',
    author_email ='Mohammedshifin1521@gmail.com',
    package =find_packages ,
    install_requires =get_requirements('requirements.txt'),
)