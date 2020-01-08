from setuptools import setup

setup(     
    name="core",
    version="0.1",
    packages=['core','scripts'],
    install_requires=['jinja2'],
    description="Simple Python web framework from scratch",
    author='Harin Ramesh',
    project_urls={
        "Source Code": "https://github.com/iamHarin17/core",
    },
    entry_points = {
        'console_scripts': ['core=scripts.console_commands:main'],
    }
)
