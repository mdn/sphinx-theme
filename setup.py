import os
import re
import codecs
from setuptools import setup


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='mdn-sphinx-theme',
    version=find_version('mdn_theme', '__init__.py'),
    description='A Sphinx theme for the Mozilla Developer Network',
    long_description=read('README.rst'),
    author='Mozilla & Contributors',
    author_email='mdn-dev@mozilla.com',
    packages=['mdn_theme'],
    zip_safe=False,
    include_package_data=True,
    install_requires=['sphinx'],
    url='https://github.com/mdn/sphinx-theme',
    license='MPL 2.0',
    keywords='sphinx extension theme mdn',
    classifiers=[
        'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ]
)
