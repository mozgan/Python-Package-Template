#!/usr/bin/env python3

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="template",
    version="0.1",
    author="mozgan",
    author_email="mozgan@gmail.com",
    description="Package template for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mozgan/Python-Package-Template",
    packages=setuptools.find_packages(),
    project_urls={
        "Bug Tracker": "https://github.com/mozgan/Python-Package-Template/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='python, package, template',
)

