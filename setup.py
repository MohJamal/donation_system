from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in donation_system/__init__.py
from donation_system import __version__ as version

setup(
	name='donation_system',
	version=version,
	description='Donation System App',
	author='MohJamal',
	author_email='x@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
