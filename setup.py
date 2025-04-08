from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommender-System-using-Machine-Learning-End-to-End-with-Deployment_Project-22"
AUTHOR_USER_NAME = "abhishekptl16"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="ABHISHEK PATEL",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhishekpatel16/Books-Recommender-System-using-Machine-Learning-End-to-End-with-Deployment_Project-22",
    author_email="abhishekpatel0771@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)