# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_jbanks", # the name that you will install via pip
    version="1.1.4",
    author="Jen Banks",
    author_email="jenniferbanks8585@gmail.com",
    description="DS helper",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/JenBanks8585/lambdata-JenBanks",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)