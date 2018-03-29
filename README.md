# README

This repo is my toolkit of ansible roles and examples. It is not aimed at any specific project,
 rather it is for generically useful scripts. A side effect is I will also be using it for setting
 up dev machines. It is my go-to 'I broke my machine and need to reinstall everything' repo.

## Getting started
Run the bash script that sets up the dependencies for Ansible and installs it.

```
$ sudo installers/XUbuntu_1704.sh
```


## Running Playbooks

- Simple playbook on local machine: ```$ ansible-playbook -i hosts /path/to/playbook.yml```