"""Setup app from setup.cfg
"""


from setuptools import find_packages, setup

setup(
    packages=find_packages(exclude="tests"),
    tests_require=["tox", "requests", "click", "pytest", "pytest-cov"],
    install_requires=["click", "requests"],
    setup_requires=["pytest-runner", "pytest-flake8"],
    entry_points={"console_scripts": ["pyndv=pyndv.__main__:main"]},
)
