from setuptools import setup, find_packages

from b3cal import __version__

setup(
    name='b3cal',
    version=__version__,

    url='https://github.com/joseparreiras/b3cal',
    author='José Antunes Neto',
    author_email='joseparreiras@gmail.com',
    description='A package for Brazilian financial market calendar and holidays',
    long_description=open('README.md').read(),
    packages = find_packages(),
    install_requires=[
        'pandas',
        'DateTime'
    ],
    include_package_data=True,
    package_data={'': ['data/holidays.csv']},
)