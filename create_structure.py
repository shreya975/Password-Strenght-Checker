import os

structure = {
    "password-strength-checker": {
        "src": [
            "__init__.py",
            "validator.py",
            "scorer.py",
            "patterns.py",
            "suggestions.py",
            "checker.py"
        ],
        "data": [
            "common_passwords.txt"
        ],
        "tests": [
            "test_checker.py"
        ],
        "root_files": [
            "README.md",
            "requirements.txt",
            "main.py"
        ]
    }
}

def create_structure(base_path="."):
    project = structure["password-strength-checker"]

    root_dir = os.path.join(base_path, "password-strength-checker")
    os.makedirs(root_dir, exist_ok=True)

    # Create subfolders and files
    for folder, files in project.items():
        if folder == "root_files":
            for f in files:
                open(os.path.join(root_dir, f), "w").close()
        else:
            folder_path = os.path.join(root_dir, folder)
            os.makedirs(folder_path, exist_ok=True)
            for f in files:
                open(os.path.join(folder_path, f), "w").close()

    print("Project structure created successfully!")


if __name__ == "__main__":
    create_structure()
