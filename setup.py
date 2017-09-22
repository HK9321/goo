# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='goo',
    version='0.0.1',
    author='Seamile',
    author_email='lanhuermao@gmail.com',
    license='MIT',

    zip_safe=False,
    install_requires=["pexpect>=3.3.0"],
    scripts=['goo']
)
