# PhysiCell_project_launcher
Warning!! Experimental Prototype backup your directory!!
!! No safety has been added yet!!

Prototype project loader for PhysiCell
install into PhysiCell main directory

Uses the built in Make Reset and then swaps the files from a projects directory
Run python Projects.py <project_name> to switch projects
all projects will be stored in ./projects directory
- [ ] **TO DO**: make these backup the current files on switch
optionally, directory created on first run

If a project name isn't found optionally create project from template files
template files should include (at the moment all are blank besides the Makefile):
- main.cpp
- PhysiCell_settings.xml
- Makefile (need to have Makefile_Template in main PhysiCell directory)
- project_name.cpp
- project_name.h

Currently just works on Linux
