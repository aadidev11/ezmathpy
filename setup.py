from setuptools import setup, find_packages

setup(
    name="ezmathpy",
    version="0.1.0",
    author="aadidev11",
    author_email="axdtutorials@gmail.com",  # Replace with your email
    description="Lightweight Python math utility library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aadidev11/ezmathpy.git",  # Replace with your repo URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
