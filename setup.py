from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='niel smith first package for hackathon',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/nsmith7123/mypackage',
    author='Niel Smith',
    author_email='nsmith7123@gmail.com'
)
