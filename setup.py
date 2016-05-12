#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    import warnings
    warnings.warn("`setuptools` not found, using `distutils` instead.")
    from distutils.core import setup  # this is just as a fallback

setup(
        name='sympy_monkey_patches',
        version='1.0',
        description='Monkey patches to the official SymPy 1.0',
        long_description="""
Monkey patches that can be applied before they make to the official releases.

The version of this monkey patch package matches the SymPy version it patches.
""",
        license='MIT',
        author='Haimo Zhang',
        author_email='zh.hammer.dev@gmail.com',
        url='https://github.com/haimoz/sympy_monkey_patches',
        requires=['sympy(==1.0)',],
        install_requires=['sympy==1.0',],
        packages=['sympy_monkey_patches'],
        classifiers=[
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 3',
                'Topic :: Utilities',
                ],
        )
