import os

PROJECT_NAME="Coder_Buddy"

folders=[
    "config",
    "constants",
    "data",
    "utils",
    "exceptions",
    "logger",
    "notebooks",
    "src",
    f"src/{PROJECT_NAME}/components",
    f"src/{PROJECT_NAME}/constants",
    f"src/{PROJECT_NAME}/entity",
    f"src/{PROJECT_NAME}/utils",
    f"src/{PROJECT_NAME}/agents",
]



for folder in folders:
    if os.path.exists(folder):
        print(f"Folder '{folder}' already exists. Skipping creation.")
    else:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")
    init_file = os.path.join(folder, "__init__.py")
    if not os.path.exists(init_file):
        print(f"Creating __init__.py in folder: {folder}")
        with open(init_file, "w") as f:
            pass
    else:
        print(f"__init__.py already exists in folder: {folder}")