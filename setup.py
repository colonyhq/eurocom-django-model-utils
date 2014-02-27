import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = '0.3.5'

setup(
    name='edmu',
    version=version,
    description="A collection of Django Model utility classes.",
    long_description='\n\n'.join([read("README.rst"), read("CHANGES.rst")]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: Other/Proprietary License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords='eurocom edmu django model utilities',
    author='Eurocom',
    author_email='sysadmin@eurocom.co.za',
    maintainer='Eurocom',
    maintainer_email='sysadmin@eurocom.co.za',
    url='https://bitbucket.org/eurocom/eurocom-django-model-utils',
    license='Other/Proprietary License',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'django',
        'django-uuidfield==0.4.0',
    ],
    setup_requires=[
        'setuptools',
    ],
)