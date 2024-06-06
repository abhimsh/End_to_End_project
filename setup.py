from setuptools import find_packages, setup

def find_all_requirements():
    """
    This function will read the requirements.txt and add them as dependecies for local package
    """
    requirements = []
    with open("requirements.txt") as file_obj:
        all_requirements = file_obj.readlines()

    requirements = [req.replace("\n", "") for req in all_requirements if "-e ." not in req]

    return requirements

setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="Abhilash M",
    author_email="abhimshedu@gmail.com",
    packages=find_packages(),
    install_requires=find_all_requirements()
)