from distutils.dir_util import copy_tree
from os import path

TEMPLATE_PATH = "core/conf/projct_template"
def create(name):
    if path.exists(name):
        print("Folder with same exists")
        return
    copy_tree(TEMPLATE_PATH,name)
    print("Project created successfully")
