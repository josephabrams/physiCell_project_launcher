#!/usr/bin/env python3
import argparse
import fileinput
import os
import subprocess

parser=argparse.ArgumentParser(description='Take in project name to switch or create.')
parser.add_argument('project_name', type=str, help='name of project')
args= parser.parse_args()
project_name=args.project_name
parent_dir = "./projects"
path = os.path.join(parent_dir, project_name)
make_path=os.path.join(path,'Makefile')



cpp_file=project_name+".cpp"
h_file=project_name+".h"
cpp_path=os.path.join(path,cpp_file)
h_path=os.path.join(path,h_file)
main_file="main.cpp"
main_path=os.path.join(path,main_file)
config_file="config.xml"
config_path=os.path.join(path,config_file)
# backup everything
#os.popen('make archive')
if os.path.exists(path):
    switch_answer=input(f'switch project to {project_name}? ([y]es/[n]o')
    if switch_answer!= 'y' or 'yes' or 'Yes' or 'YES':
        exit()
    #switch to this project and set everything up
    os.popen('make reset') #should probably add a line to save stuff
    with fileinput.FileInput(make_path, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("joes_project", project_name), end='')
    os.popen(f'cp {make_path} ./')
    os.popen(f'cp {cpp_path} ./custom_modules/')
    os.popen(f'cp {h_path} ./custom_modules/')
else:
    #optionally create project
    print(f'create new project named {project_name} ?')
    answer=input('[y]es/[n]o ?') 
    if answer== 'y' or 'yes' or 'Yes':
        if os.path.exists(parent_dir)!=True:
            os.mkdir(parent_dir)
        os.mkdir(path)
        # create the template files
        #./project/templates/Makefile_template
        # etc
    else:
        exit()

    
