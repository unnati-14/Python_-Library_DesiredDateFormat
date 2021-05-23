import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DesiredDateFormat",
    version="1.0.0",
    author="Unnati Singh",
    author_email="singhunnati1401@gmail.com",
    description="A library which converts any date into desired date format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unnati-14/Python_-Library_DesiredDateFormat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2',
)