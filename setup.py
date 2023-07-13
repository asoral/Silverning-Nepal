from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in silverlining_nepal/__init__.py
from silverlining_nepal import __version__ as version

setup(
	name="silverlining_nepal",
	version=version,
	description="Library",
	author="Faris",
	author_email="nand@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
