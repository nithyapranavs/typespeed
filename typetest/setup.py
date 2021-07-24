from setuptools import setup , find_packages

def req_pkg():
    with open("requirments.txt") as reqs:
        req = reqs.read().split('\n')
    return req

setup(
    name = 'typetest-cli',
    version = '1.0',
    packages = find_packages(),
    include_package_date = True,
    install_requires = req_pkg(),
    entry_points = {
        'console_scripts': [
            'typespeed = main.code:main'
        ]
    })