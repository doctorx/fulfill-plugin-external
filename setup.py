import pathlib
from setuptools import setup, find_namespace_packages
from pkg_resources import parse_requirements

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in parse_requirements(requirements_txt)
    ]

README = (pathlib.Path()/pathlib.Path('README.md')).open().read()

setup(
    name='fulfill-plugin-external',
    version='0.4.1',
    author='Doctorx',
    summary='Fulfillment external plugin',
    long_description=README,
    packages=find_namespace_packages(include=['fulfill.*', 'fulfill.plugins.*']),
    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=3.8, <4',
)
