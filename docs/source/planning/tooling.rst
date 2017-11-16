Tooling Plan
============

Backend
-------

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
            - Sphinx-autobuild
            - Sphinx-rtd-theme
- Continuous Integration: Circle CI (if applicable)

Frontend
--------
- Template: Bootstrap/Bootswatch (Lux) https://bootswatch.com/lux/
- HTML Version: 5
- CSS Version: 3
- Javascript
    - Version: TBD
    - Minifier: None - Javascript will be unminified to allow for inspection
