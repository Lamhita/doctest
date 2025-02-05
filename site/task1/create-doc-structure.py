import os

# Define the documentation structure
docs_structure = {
    "architecture": ["system_components.md", "user_management.md"],
    "security": ["multi_tenancy.md", "rbac.md"],
    "sessions": ["session_management.md", "rate_limits.md"],
    "users": ["user_status_transitions.md", "kyc_verification.md"],
    "visuals": ["system_architecture.md", "user_lifecycle.md"]
}

# List of standalone files
standalone_files = ["index.md", "why-multi-tenancy.md"]

# Base directory where the script and index.md are located
base_dir = os.path.dirname(os.path.abspath(__file__))

def create_folder_structure():
    """Creates the folder and file structure for the documentation."""
    for folder, files in docs_structure.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)  # Create folders if they don't exist

        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write(f"# {file.replace('.md', '').replace('_', ' ').title()}\n\n")

    # Create standalone files
    for file in standalone_files:
        file_path = os.path.join(base_dir, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {file.replace('.md', '').replace('_', ' ').title()}\n\n")

    print("📂 Documentation folder structure successfully created!")

if __name__ == "__main__":
    create_folder_structure()
