Development Plan
================

Stage 0) Devbox setup
---------------------

This stage will be setting up a computer to develop on.

- [x] Install the OS
- [x] Configure it to personal liking (.bashrc, code editor, browser, etc...)
- [x] Create project directory & subdirectories
- [x] Install Python 3.6.1 globally
- [x] Install Pylint globally
- [x] Install YAPF globally
- [x] Install Coverage globally
- [x] Install virtualenvmanager globally (including the updated .bashrc)
- [x] Make a devops virtualenv ``$ mkvirtualenv -a `pwd` --python=`which python3.6` devops``
- [x] Make a website virtualenv
- [x] Make a docs virtualenv

Stage 1) Devops for Devbox
--------------------------

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

Stage 2) Documentation Setup
----------------------------

- [x] Create a setup.py for the docs folder
- [x] Create a README.md for the docs folder
- [x] Use it to install sphinx
- [x] Complete the sphinx-quickstart
- [x] Install necessary extensions
- [x] Transfer the planning documents to the sphinx documentation

Stage 3) Website Setup
----------------------

- [] Create a setup.py for the website folder
- [] Create a README.md for the website folder
- [] Use the setup.py to install Django
- [] ``$ django-admin startproject portfolio``
- [] Create a 'Hello World' landing page
- [] Set up tests for the landing page

Stage 4) Get it running
-----------------------
- [] Set up a ReadTheDocs to host the documentation
- [] Set up a Heroku project for hosting the website
    - [] ?
    - [] ?
    - [] ?
    - [] ?
    - [] ?
