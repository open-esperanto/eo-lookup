import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r') as f:
    README = f.read()

setup(
    name="eo_lookup_revo",
    version="1.0.1",
    description="GPL-licensed ReVo content for eo-lookup",
    long_description=README,
    url="https://github.com/open-esperanto/eo-lookup",
    author="Open Esperanto",
    author_email="admin@libraro.net",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3"
    ],
    keywords="esperanto revo",
    py_modules=["eo_lookup_revo"],
    data_files=[('', ['eo_lookup_revo.json'])])
