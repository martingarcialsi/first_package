from setuptools import setup, find_packages

if __name__ == "__main__":

    setup(name = "mypackage",
    decription = "Package to learn how to use packages with gtihub",
    license = "MIT",
    url = "https://github.com/sergiobautistalsi/first_package",
    version = "0.0.1",
    author = "Sergio Sosa",
    email = "sergio.bautista@logicsource.com",
    long_description = open("README.md").read(),
    packages = find_packages(),
    zip_safe = False,
    install_requires = [],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independet",
        "Programming Language :: Python",
    ],)