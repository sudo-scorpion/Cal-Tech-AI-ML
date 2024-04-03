import os

# Define the directory structure
structure = {
    'flask_project': {
        'app': {
            '__init__.py': '',
            'templates': {},
            'static': {},
            'models': {
                '__init__.py': '',
                'models.py': ''
            },
            'routes': {
                '__init__.py': '',
                'view_routes.py': '',
                'api_routes.py': ''
            },
            'services': {
                '__init__.py': '',
                'business_logic.py': ''
            },
            'utils': {
                '__init__.py': '',
                'helper_functions.py': ''
            },
            'forms': {
                '__init__.py': '',
                'form_definitions.py': ''
            }
        },
        'migrations': {},
        'tests': {
            '__init__.py': '',
            'test_config.py': '',
            'test_models.py': '',
            'test_routes.py': ''
        },
        'config.py': '',
        '.env': '',
        'requirements.txt': '',
        'run.py': ''
    }
}

def create_structure(base_path, structure):
    """Recursively creates directories and files based on the `structure` dictionary."""
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # It's a directory, create it and recurse into it
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # It's a file, create it
            with open(path, 'w') as f:
                f.write(content)

# Using the current directory as the base
base_path = os.getcwd()

# Create the project structure
create_structure(base_path, structure['flask_project'])

print("Flask project structure created successfully.")
