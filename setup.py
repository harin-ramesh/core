from setuptools import setup

setup(     
    name="core",
    version="0.1",
    packages=['core','scripts'],
    install_requires=['jinja2'],
    description="Light weight web framework",
    author='Harin Ramesh',
    project_urls={
        "Source Code": "https://github.com/iamHarin17/core",
    },
    entry_points = {
        'console_scripts': ['core=scripts.createproject:main'],
    }
)
