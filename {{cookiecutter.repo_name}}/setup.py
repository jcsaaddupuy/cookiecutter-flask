#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = open("requirements.txt").read()
test_requirements = open("requirements-tests.txt").read()

import version

setup(
    name='{{ cookiecutter.repo_name }}',
    version=version.APP_VERSION,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme,
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    # configure the default command line entry point.
    entry_points={
        'console_scripts': [
            '{{cookiecutter.repo_name}}-manage = {{cookiecutter.repo_name}}.manage:main',
        ]
    },



    include_package_data=True,
    install_requires=requirements,
    license="WTFPL",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
