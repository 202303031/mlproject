from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    # Use 'with open' to properly open the file object
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters (\n) from each package name
        requirements = [req.replace("\n", "") for req in requirements]

        # Safely filter out the editable install flag if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Dhruv',
    author_email='dhruvramani5566@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')  # Make sure this matches your file name exactly
)