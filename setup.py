from setuptools import setup, find_packages

setup(
    name='gitsync',
    version='0.1.0',
    packages=find_packages(include=['gitsync', 'gitsync.*']),
    install_requires=[
        'requests==2.25.1',
        'pytest==6.2.2'
        ],
    setup_requires=[
        'pytest-runner',
        'flake8'
        ],
    tests_require=['pytest']
)
