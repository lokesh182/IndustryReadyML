from setuptools import setup,find_packages
from typing import List

    
def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of required packages
    '''
    HYPHEN_DOT = '-e .'
    requirements = []
    with open(file_path) as f_obj:
        requirements = f_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    return requirements




setup(
    name='MLProject',
    version='0.0.1',
    author='Lokesh',
    author_email='lokeshbapte.18@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)