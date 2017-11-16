# Portfolio of Joel Tannas

Current status: Planning Stage

This will be the source code for a website that shows off my code abilities using javascript and using links to my Github projects.

## Tooling Plan

- Backend:
  - OS: XUbuntu 17.04
  - Hosting Service: Heroku
  - Version Control:
    - Software: Git
    - Central Repository: Github
  - Language: 
    - Name: Python
    - Version: 3.6.1
    - Linter: PyLint3
    - Format:
      - Standard: PEP 008
      - Formatter: YAPF
    - Testing:
      - Framework: Unittest
      - Coverage: Coverage
  - Devops:
    - Location: ~/portfolio/devops
    - Framework: Ansible 2.4
  - Webserver:
    - Location: ~/portfolio/website
    - Framework: Django 1.11
  - Documentation:
    - Location: ~/portfolio/docs
    - Framework:
      - Name: Sphinx/RST
      - Extensions:
        - Sphinx-Autodoc
        - Sphinx-Apidoc
  - Continuous Integration: Circle CI (if applicable)
- Frontend:
  - Template: Bootstrap/Bootswatch (Lux) https://bootswatch.com/lux/
  - HTML Version: 5
  - CSS Version: 3
  - Javascript
    - Version: TBD
    - Minifier: None - Javascript will be unminified to allow for inspection
    
## Development Plan

### Stage 0) Devbox setup
This stage will be setting up a computer to develop on.

- [x] Install the OS
- [x] Configure it to personal liking (.bashrc, code editor, browser, etc...)
- [x] Create project directory & subdirectories
- [x] Install Python 3.6.1 globally
- [x] Install Pylint globally
- [x] Install YAPF globally
- [x] Install Coverage globally
- [x] Install virtualenvmanager globally (including the updated .bashrc)
- [x] Make a devops virtualenv ```$ mkvirtualenv -a `pwd` --python=`which python3.6` devops```
- [x] Make a website virtualenv
- [x] Make a docs virtualenv

### Stage 1) Devops for Devbox
This stage will commit all the needed setup from stage 0 to code.

- [x] Create a setup.py file to install the devops packages
- [x] Create an installer script for devops that handles the installation of external dependencies
- [x] Create Ansible roles for the needed global packages
  - [x] Python3.6
  - [x] YAPF
  - [x] Pylint
  - [x] Coverage
  - [x] virtualenvmanager
- [x] *Optional* Create Roles for personal settings
- [x] Create a playbook for applying the roles to the localhost
- [x] Run the playbook against the localhost to confirm setup
- [x] Create a README.md for devops specific information
