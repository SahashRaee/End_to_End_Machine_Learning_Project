import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H-%M-%S"
)
# logging.info("logging is configured successfully.")
# logging.warning("This is a warning log.")
# logging.error("This is an error log.")

project_name = "my_project"

list_of_files=[
    ".github/workflows/.gitkeep", 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/config_entity.py",
    "config/config.yaml",
    "schema.yaml",
    "params.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory{filedir} for the file: {filename}")

    if(not os.path.exists(filepath) or (os.path.getsize(filepath) ==0)):
        with open (filepath, 'w'):
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists.")
    
