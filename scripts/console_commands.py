import argparse
from os import path
from distutils.dir_util import copy_tree

TEMPLATE_PATH = "core/conf/projct_template"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', type=str, nargs='+',
                         help='project managment commands')
    args = parser.parse_args() 
    if args.operation[0] == 'create-project':
        try:
            create_project(args.operation[1])
        except IndexError as e:
            print("!!Not enough arguments")
            
def create_project(name):
    if path.exists(name):
        print("Folder with same exists")
        return
    copy_tree(TEMPLATE_PATH,name)
    print("Project created successfully")
