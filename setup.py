"""Setup app from setup.cfg
"""

from setuptools import setup, find_packages

setup(
    packages=find_packages(exclude='tests'),
    tests_require=['tox', 'requests', 'click'],
    install_requires=['click', 'requests'],
    entry_points={
        'console_scripts': [
            'pyndv=pyndv.__main__:main'
        ],
    }
)
