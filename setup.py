from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:  # for reading requirements from requirements .py
    ''' this function will return the list of requirements '''
    requirements=[]
    with open("requirements.txt") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements




setup(
    
    name="my_ml_project",
    version="0.0.1",
    author="Dharmendra Singh",
    author_email="chauhandharmendra293@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    # this is manual way to add dependencies
    #[
    #   "numpy",
    #    "pandas",
    #    "scikit-learn",
     #   "flask",
     #   "gunicorn"
    #],
    #description="A machine learning project setup"
    
    
    
)