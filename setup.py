from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = ' Python package that generates strong and random passwords.'
LONG_DESCRIPTION = ' Python package that generates strong and random passwords. You can specify the length and complexity of the password (e.g., including uppercase letters, lowercase letters, numbers, and special characters). The package should return a randomly generated password'

# Setting up
setup(
    name="PyKeyPass",
    version=VERSION,
    author="Chahid Ahmadi",
    author_email="<chahid.ahmadi@cloudsoftware.tn>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['string', 'random'],
    keywords=['password', 'random'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)