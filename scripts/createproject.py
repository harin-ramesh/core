import os
import argparse

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
            
def create_project(a):
    pass
