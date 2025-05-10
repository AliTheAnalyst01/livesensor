from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirement_list = list[str]=[]

    return requirement_list


setup(
    name = "sensor",
    version = "0.0.1",
    author = "Faizan",
    author_email = "faizanzaidy78@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),  
)
