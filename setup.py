'''
Created on 03-Sep-2019

@author: elango
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="find_files",
    version="0.0.1",
    author="Elango SK",
    author_email="elango111000@gmail.com",
    description="To find the file by using name and extension for your given directory",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)