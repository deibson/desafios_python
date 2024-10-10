from setuptools import setup, find_packages


with open("README.md", "r") as f:
    page_description = f.read()


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="package_name",
    version="0.0.1",
    author="my_name",
    author_email="my_email",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_repository_project_link",
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": ["pytest", "twine"],
    },
    license="MIT",
    zip_safe=False,
    test_suite="unittest",
)

