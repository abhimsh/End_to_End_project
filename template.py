import os
from pathlib import Path

project_name = "DiamondPricePrediction"

list_of_files= [
    ".github/workflows/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils/__init__.py",
]

cwd = os.getcwd()
for file in list_of_files:
    # To get system independent path \ or /
    file_path = Path(file)
    # get the file path and directory path separately
    folder, file = os.path.split(file_path)
    # Create a directory, if already present ignore
    if folder != "":
        os.makedirs(folder, exist_ok=True)
    # Create a file is not exists in path
    if (not os.path.exists(file_path)) or \
        (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as file_obj:
            pass
    else:
        print(f"{file_path} already exists")
    