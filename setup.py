from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='EDSA',
    description='EDSA - Recursion and Sorting Functions',
    long_description=open('README.md').read(),
    install_requires=['none'],
    url='https://github.com/<RidhaMoosa>/<recursion_sorting>',
    author='<Ridha Moosa>',
    author_email='<drridhamoosa@gmail.com>'
)
