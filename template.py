import os # for creating directories
from pathlib import Path # for creating directories and files
import logging # for logging messages in console

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') #, datefmt='%(asctime)s %(message)s')

project_name = "Chicken-Disease-Classification"

list_of_files = [
    ".github/workflows/.gitkeep", # git keep file
    f"src/{project_name}/__init__.py", # init file
    f"src/{project_name}/components/__init__.py", # components init file
    f"src/{project_name}/utils/__init__.py", # utils init file
    f"src/{project_name}/utils/common.py", # common file
    # f"src/{project_name}/logging/__init__.py", # logging init file
    f"src/{project_name}/config/__init__.py", # config init file
    f"src/{project_name}/config/configuration.py", # configuration file
    f"src/{project_name}/pipeline/__init__.py", # pipeline init file
    f"src/{project_name}/entity/__init__.py", # entity init file
    f"src/{project_name}/constants/__init__.py", # constants init file
    "config/config.yaml", # config file
    "dvc.yaml", # dvc file
    "params.yaml", # params file
    "requirements.txt", # requirements file
    "setup.py", # setup file
    "trials.ipynb", # trials file
    # "schema.yaml", # schema file
    # "main.py", # main file
    # "app.py", # app file

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # create directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}") # log the creation of the directory

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # check if the file exists and is empty
        with open(filepath, "w") as f: # create the file "w" for write 
            pass # do nothing
            logging.info(f"Creating empty file: {filepath}") # log the creation of the file 

    else:
        logging.info(f"{filename} is already exists")