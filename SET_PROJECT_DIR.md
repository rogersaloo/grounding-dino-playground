# Setup ML project Directory
## Description
When setting up a new ML project directrory follow the steeps;

## Create Directory and main files
1. Create the directory
```mkdir new_project```
2. ```cd``` the new_project directory and begin making files.
- ```touch README.md``` File containing the description of the project. Refer to [template](here).
- ```touch CHANGELOG.md``` File containing the changes occuring in the project. Refer to [template](here).
- ```touch CONTRIBUTING.md``` File highlighting the rules of contributing to the project and version control usage.
- ```touch .gitignore``` file containing the files and directories to ignore while sending to version control.  
    ```vim .gitignore``` and add the following.
    Press ```i``` to begin editing.
    ```
    # .gitnore
    venv
    credentials
    __pycache__
    .env
    dataset
    runs
    checkpoint
    ```
    Press ```Esc``` > ```:``` > ```wq``` to save and exit vim.
- ```requirements.txt``` contains the packages used in the 
### Create Virtual environment
1. Create the virtual environment to use for isolating and installing the required packages and dependancies for the project.
    ``` python3 -m venv venv
        source venv/bin/activate
        python3 -m pip install pip setuptools wheel
    ```
2. To activate the virtual environments.
    - For windows users:
        Set the execution policy on a Windows computer to be able to run the environment by running the script ```Set-ExecutionPolicy Unrestricted -Scope``` Process on Windows powershell.

        ```.\venv\Scripts\activate ``` and activate the environment 
    - For a mac/Linux use: 
        ```source venv/bin/activate```. And activate the environment 

        By now the project tree should appear like this.
#### Project tree
    |--new_project
        |--CONTRIBUTING.md
        |--CHANGELOG.md
        |--README.md
        |--.gitignore
        |--requirements.txt

### Setup
The setup file provides instructions on how to setup the virtual environment. 
1. ```touch setup.py``` and start extraction of the packages from the ```requirements.txt```
    ```
    # setup.py
    from pathlib import Path
    from setuptools import find_namespace_packages, setup

    # Load packages from requirements.txt
    BASE_DIR = Path(__file__).parent
    with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
        required_packages = [ln.strip() for ln in file.readlines()]
    ```
    The core of setup is to describe how to setup our packages and dependacies. It contains the metadata together with the required python version and the list of the packages.
    ```
    # setup.py
    setup(
        name="name_of_project",
        version=0.1,
        description="Description of the machine learning project",
        author="Name of author",
        author_email="emailof@author.com",
        url="https://urltotheauthor.com/",
        python_requires=">=3.7",
        install_requires=[required_packages],
    )
    ```
#### Project tree
    |--new_project
        |--setup.py
        |--CONTRIBUTING.md
        |--CHANGELOG.md
        |--README.md
        |--.gitignore
        |--requirements.txt

 ### Install dependencies
 1. Install the required packages and their dependancies using pip.
- First install ```pipreqs``` to use in writing the install packages to the requirements file. ```pip install pipreqs```.
- Normally we would use ```pip freeze >> requirements.txt``` but it has a shortcoming in copyig packages and their dependencies resulting in conflicts during installation. We solve this using ```pipreqs```. Run
 ```pip install <package name>```
 - After installation of the dependacies use ```pipreqs requiremets.txt```

    In a case where the requirements.txt file exists with all the dependencies run ```pip install -r requirements.txt```
- The ```requirements.txt``` file should now appear as:
    ```
    requirements.txt
    <PACKAGE>==<VERSION>  # exact version
    <PACKAGE>==<VERSION>  # above version
    <PACKAGE>             # no version
    ```

### Configurations

Create configuration directory to store the configurations required in the project. ```mkdir config```
- ```args.json``` contains the arguments needed in the config.
- ```config.py``` contains the code for mapping the json config key values.
- sample args.py
    ```
    {
    "shuffle": true,
    "subset": null,
    "min_freq": 75,
    "lower": true,
    "stem": false,
    "analyzer": "char",
    "ngram_max_range": 7,
    "alpha": 1e-4,
    "learning_rate": 1e-1,
    "power_t": 0.1
    }

    ```
- sample ```config.py```
    ```
    # config.py
    from pathlib import Path

    # Directories
    BASE_DIR = Path(__file__).parent.parent.absolute()
    CONFIG_DIR = Path(BASE_DIR, "config")

    ```

### Project
Contains the scripts used for creating the model. Different modules are seperated into different scripts. For instance
```mkdir model_name``` and create all the required files using ```touch <file-name>```

    |--model_name
        |--main.py
        |--models.py
        |--train.py
        |--preprocess.py
        |--data.py
        |--utils.py

## Styling and Linting
We can set up the project to have ```consistency``` and ```automation``` to allow standard code and allow well formated and linted code before pushing to the repo.
- Add the packages 
    ```
    pip install black
    ```
- Add the following code to the ```setup.py``` to apply the packages across the machine.
    ```
    # setup.py
    style_packages = [
        "black==22.3.0",
        "flake8==3.9.2",
        "isort==5.10.1"
    ]

    # Define our package
    setup(
        ...
        extras_require={
            "dev": docs_packages + style_packages,
            "docs": docs_packages,
        },
    )
    ```
- Before using the tool for styling configure balck using the ```touch pyproject.toml``` file. Add the following in the file.
    ```
    # Black formatting
    [tool.black]
    line-length = 80
    include = '\.pyi?$'
    exclude = '''
    /(
        .eggs         # exclude a few common directories in the
        | .git          # root of the project
        | .hg
        | .mypy_cache
        | .tox
        | venv
        | _build
        | buck-out
        | build
        | dist
    )/
    '''
    ```
- To use black for styling on the CLI run. ```black .```

## Preperation for Release
When deploying the application there are several changes that we'll consider making on the dev code.
### Logging
Next we keep logging for tracking of the events that occur within the application.
e```mkdir config```
- ```args.json``` contains the arguments needed in the config.
- ```config.py``` contains the code for mapping the json config 

First update the ```config.py``` earlier with the location of the logs by adding.
```# config/config.py
LOGS_DIR = Path(BASE_DIR, "logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)
```
Next add the logger for the application stating the levels of logging and the maximum logs allowable per level.
```
# config/config.py
import logging
import sys
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "minimal": {"format": "%(message)s"},
        "detailed": {
            "format": "%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "minimal",
            "level": logging.DEBUG,
        },
        "info": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "info.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.INFO,
        },
        "error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "error.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.ERROR,
        },
    },
    "root": {
        "handlers": ["console", "info", "error"],
        "level": logging.INFO,
        "propagate": True,
    },
}
```
We load the logger configuration dictionary in the following way.
```# config/config.py
from rich.logging import RichHandler
logging.config.dictConfig(logging_config)
logger = logging.getLogger()
logger.handlers[0] = RichHandler(markup=True)  # pretty formatting

# Sample messages (note that we use configured `logger` now)
logger.debug("Used for debugging your code.")
logger.info("Informative messages from your code.")
logger.warning("Everything works but there is something to be aware of.")
logger.error("There's been a mistake with the process.")
logger.critical("There is something terribly wrong and process may terminate.")
```
Finally all the print statements within the code that we have written in dev will be replaced with logging.
```
print("✅ Saved data!")
```
Replace with:
```from config.config import logger
logger.info("✅ Saved data!")
```

## Resources 
1. Part of the code steps taken from
``` 
@article{madewithml,
    author       = {Goku Mohandas},
    title        = { Packaging - Made With ML },
    howpublished = {\url{https://madewithml.com/}},
    year         = {2022}
}
 ```