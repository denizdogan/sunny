import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sunny",
    version = "0.0.1",
    author = "Deniz Dogan",
    author_email = "deniz@dogan.se",
    description = "Yet another minimalistic interface to Solr, "
                  "with support for parameter keys with multiple values.",
    license = "BSD",
    keywords = "solr search",
    url = "http://www.dogan.se/sunny",
    packages=['sunny'],
    long_description=read('README'),
    requires=['urllib3'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
    ],
)
