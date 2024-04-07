import os
import sys

def create_project_structure(structure, base_path=''):
    for name, value in structure.items():
        current_path = os.path.join(base_path, name)
        if isinstance(value, dict):  # It's a directory
            os.makedirs(current_path, exist_ok=True)
            create_project_structure(value, current_path)  # Recurse into the directory
        else:  # It's a file
            with open(current_path, 'w') as f:
                f.write(value)  # Create an empty file for now

# Project structure definition including a models directory
project_structure = {
    "ShoppingApp": {
        "app": {
            "__init__.py": "",
            "api": {
                "__init__.py": "",
                "namespaces": {
                    "__init__.py": "",
                    "auth_ns.py": "",
                    "product_ns.py": "",
                    "cart_ns.py": "",
                    "checkout_ns.py": "",
                }
            },
            "models": {  # Added models directory
                "__init__.py": "",
                "user.py": "",
                "product.py": "",
                "category.py": "",  # Example for additional model
            },
            "schemas": {
                "__init__.py": "",
                "user_schema.py": "",
                "product_schema.py": "",
            },
            "services": {
                "__init__.py": "",
                "auth_service.py": "",
                "product_service.py": "",
                "cart_service.py": "",
                "checkout_service.py": "",
            },
            "data": {
                "__init__.py": "",
                "data_store.py": "",
            }
        },
        "run.py": ""
    }
}

# Specify the base path where you want to create the project
base_path = sys.argv[1] if len(sys.argv) > 1 else ''

# Create the project structure
create_project_structure(project_structure, base_path)

print(f"Project structure has been created at {base_path}")
