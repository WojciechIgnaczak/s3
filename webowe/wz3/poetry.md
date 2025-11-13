u334535@user-Precision-3460:~/Pulpit$ cd webowe_project/
u334535@user-Precision-3460:~/Pulpit/webowe_project$ curl -sSL https://install.python-poetry.org | python3 -
Retrieving Poetry metadata

# Welcome to Poetry!

This will download and install the latest version of Poetry,
a dependency and package manager for Python.

It will add the `poetry` command to Poetry's bin directory, located at:

/home/u334535/.local/bin

You can uninstall at any time by executing this script with the --uninstall option,
and these changes will be reverted.

Installing Poetry (2.2.1): Done

Poetry (2.2.1) is installed now. Great!

To get started you need Poetry's bin directory (/home/u334535/.local/bin) in your `PATH`
environment variable.

Add `export PATH="/home/u334535/.local/bin:$PATH"` to your shell configuration file.

Alternatively, you can call Poetry explicitly with `/home/u334535/.local/bin/poetry`.

You can test that everything is set up by executing:

`poetry --version`

u334535@user-Precision-3460:~/Pulpit/webowe_project$ poetry --version
Polecenie 'poetry' nie zostało znalezione, ale można je zainstalować za pomocą:
sudo apt install python3-poetry
u334535@user-Precision-3460:~/Pulpit/webowe_project$ export PATH="/home/u334535/.local/bin:$PATH"
u334535@user-Precision-3460:~/Pulpit/webowe_project$ poetry --version
Poetry (version 2.2.1)
u334535@user-Precision-3460:~/Pulpit/webowe_project$ poetry new backend
Created package backend in backend
u334535@user-Precision-3460:~/Pulpit/webowe_project$ cd frontend
u334535@user-Precision-3460:~/Pulpit/webowe_project/frontend$ ls
Readme.md
u334535@user-Precision-3460:~/Pulpit/webowe_project/frontend$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [frontend]:      
Version [0.1.0]:  
Description []:  
Author [WojciechIgnaczak <wojciech.ignaczak@onet.pl>, n to skip]:  
License []:  
Compatible Python versions [>=3.12]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] yes
        You can specify a package in the following forms:
          - A single name (requests): this will search for matches on PyPI
          - A name and a constraint (requests@^2.23.0)
          - A git url (git+https://github.com/python-poetry/poetry.git)
          - A git url with a revision         (git+https://github.com/python-poetry/poetry.git#develop)
          - A file path (../my-package/my-package.whl)
          - A directory (../my-package/)
          - A url (https://example.com/packages/my-package-0.1.0.tar.gz)
        
Package to add or search for (leave blank to skip): 

Would you like to define your development dependencies interactively? (yes/no) [yes]   
Package to add or search for (leave blank to skip): pytest
Found 181 packages matching pytest
Showing the first 10 matches

Enter package # to add, or the complete package name if it is not listed []:
 [ 0] pytest
 [ 1] 
 > 
No package selected

Add a package (leave blank to skip): 

Generated file

[project]
name = "frontend"
version = "0.1.0"
description = ""
authors = [
    {name = "WojciechIgnaczak",email = "wojciech.ignaczak@onet.pl"}
]
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
u334535@user-Precision-3460:~/Pulpit/webowe_project/frontend$ cd ../backend/
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ ls
pyproject.toml  README.md  src  tests
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry add requests
Creating virtualenv backend-f8bJNHXL-py3.12 in /home/u334535/.cache/pypoetry/virtualenvs
Using version ^2.32.5 for requests

Updating dependencies
Resolving dependencies... (0.6s)

Package operations: 5 installs, 0 updates, 0 removals

  - Installing certifi (2025.10.5)
  - Installing charset-normalizer (3.4.4)
  - Installing idna (3.11)
  - Installing urllib3 (2.5.0)
  - Installing requests (2.32.5)

u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry add --group dev pytest black flake8
Using version ^8.4.2 for pytest
Using version ^25.9.0 for black
Using version ^7.3.0 for flake8

Updating dependencies
Resolving dependencies... (1.5s)

Package operations: 15 installs, 0 updates, 0 removals

  - Installing click (8.3.0)
  - Installing iniconfig (2.3.0)
  - Installing mccabe (0.7.0)
  - Installing mypy-extensions (1.1.0)
  - Installing packaging (25.0)
  - Installing pathspec (0.12.1)
  - Installing platformdirs (4.5.0)
  - Installing pluggy (1.6.0)
  - Installing pycodestyle (2.14.0)
  - Installing pyflakes (3.4.0)
  - Installing pygments (2.19.2)
  - Installing pytokens (0.2.0)
  - Installing black (25.9.0)
  - Installing flake8 (7.3.0)
  - Installing pytest (8.4.2)

Writing lock file
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry remove flake8
Updating dependencies
Resolving dependencies... (0.1s)

Package operations: 0 installs, 0 updates, 4 removals

  - Removing flake8 (7.3.0)
  - Removing mccabe (0.7.0)
  - Removing pycodestyle (2.14.0)
  - Removing pyflakes (3.4.0)

Writing lock file
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry remove --group dev black
Updating dependencies
Resolving dependencies... (0.1s)

Package operations: 0 installs, 0 updates, 6 removals

  - Removing black (25.9.0)
  - Removing click (8.3.0)
  - Removing mypy-extensions (1.1.0)
  - Removing pathspec (0.12.1)
  - Removing platformdirs (4.5.0)
  - Removing pytokens (0.2.0)

Writing lock file
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry add --group dev black
Using version ^25.9.0 for black

Updating dependencies
Resolving dependencies... (0.2s)

Package operations: 6 installs, 0 updates, 0 removals

  - Installing click (8.3.0)
  - Installing mypy-extensions (1.1.0)
  - Installing pathspec (0.12.1)
  - Installing platformdirs (4.5.0)
  - Installing pytokens (0.2.0)
  - Installing black (25.9.0)

Writing lock file
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry add --group dev flake8
Using version ^7.3.0 for flake8

Updating dependencies
Resolving dependencies... (0.2s)

Package operations: 4 installs, 0 updates, 0 removals

  - Installing mccabe (0.7.0)
  - Installing pycodestyle (2.14.0)
  - Installing pyflakes (3.4.0)
  - Installing flake8 (7.3.0)

Writing lock file
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry update
Updating dependencies
Resolving dependencies... (1.0s)

No dependencies to install or update
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry update pytest
Updating dependencies
Resolving dependencies... (0.2s)

No dependencies to install or update
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry show --outdated
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: backend (0.1.0)
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry env info --path
/home/u334535/.cache/pypoetry/virtualenvs/backend-f8bJNHXL-py3.12
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry run pytest
========================================== test session starts ===========================================
platform linux -- Python 3.12.3, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/u334535/Pulpit/webowe_project/backend
configfile: pyproject.toml
collected 0 items                                                                                        

========================================= no tests ran in 0.00s ==========================================
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry run black
Usage: black [OPTIONS] SRC ...

One of 'SRC' or 'code' is required.
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry run black .
All done! ✨ 🍰 ✨
2 files left unchanged.
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry config --list
cache-dir = "/home/u334535/.cache/pypoetry"
data-dir = "/home/u334535/.local/share/pypoetry"
installer.max-workers = null
installer.no-binary = null
installer.only-binary = null
installer.parallel = true
installer.re-resolve = true
keyring.enabled = true
python.installation-dir = "{data-dir}/python"  # /home/u334535/.local/share/pypoetry/python
requests.max-retries = 0
solver.lazy-wheel = true
system-git-client = false
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}/virtualenvs"  # /home/u334535/.cache/pypoetry/virtualenvs
virtualenvs.prompt = "{project_name}-py{python_version}"
virtualenvs.use-poetry-python = false
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry export -f requirements.txt --output requirements.txt --without-hashes
The requested command export does not exist.

Documentation: https://python-poetry.org/docs/cli/
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry cahce list
The requested command cahce does not exist.

Documentation: https://python-poetry.org/docs/cli/
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry cache clear pypi --all
No cache entries for pypi
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry cache clear PyPI --all
Delete 125 entries? (yes/no) [yes] yes
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry run start
Command not found: start
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry version patch
Bumping version from 0.1.0 to 0.1.1
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry version minor
Bumping version from 0.1.1 to 0.2.0
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry version major
Bumping version from 0.2.0 to 1.0.0
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ poetry version 1.2.3
Bumping version from 1.0.0 to 1.2.3
u334535@user-Precision-3460:~/Pulpit/webowe_project/backend$ 
