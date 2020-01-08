## Index
* [Installation](#installation)
* [Creating a project](#creating-a-project)

## Installation
```
git clone https://github.com/iamHarin17/core.git
cd core
python setup.py install
```

## Creating a project
```
core create-project <project-name>
```
This will a create directory with the given name.
```
project-name/
    __init___.py
    run_server.py
    settings.py
    view.py
    wsgi.py
    templates/
        index.html
```
Use the command given below to run the development server. 
```
python run_server.py
```
