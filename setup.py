from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path)->List[str]:
    '''
    This function will return the list of requirements
    '''

    requirements = []

    with open(file_path) as file_obj:

        requirements=file_obj.readlines()
        requirements=[requirement.replace("\n","") for requirement in requirements]

        if HYPEN_E_DOT in requirements:

            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name="mlproject",  # Replace with your project's name
    version="0.0.1",           # Initial version
    description="A short description of your project",
    long_description=open("README.md").read(),  # Make sure to have a README.md
    long_description_content_type="text/markdown",
    author="Sreevalli",
    author_email="sreevalli.manda@gmail.com",
    url="https://github.com/Msrevalli/MLProject1.git",  # Replace with your URL
    packages=find_packages(),  # Automatically finds and lists your packages
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Specify the Python version(s) supported
)
