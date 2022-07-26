# PhysiCell_project_launcher
Warning!! Experimental Prototype backup your directory!!
- Some safety now, currently uses make zip
- now works with 'sample_projects/template' when making new project
- 
Prototype project loader for PhysiCell
install into PhysiCell main directory

Uses the built in Make Reset and then swaps the files from a projects directory
- In terminal: $python Projects.py <project_name> 

- switch projects or create new project
- projects will be stored in ./projects directory
- [ ] **TO DO**: Make system agnostic
- [ ] **TO DO**: GUI interface
- [ ] **TO DO**: Add-on installer?
- [ ] **TO DO**: Advanced options if you want to modify core code?
- [ ] **TO DO**: Add option to select different output folders
- The projects directory is created on first run if a new project is created

If a project name isn't found optionally create project from template files
template files 
- Note: To modify Makefile (need to have Makefile_Template in main PhysiCell directory)

Currently just works on Linux
