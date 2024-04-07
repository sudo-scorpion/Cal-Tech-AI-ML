import os

bypass_flag_path = os.path.join(os.environ.get('HOME'), "bypass_role.flag")

def check_bypass_flag():
    """Check if the bypass flag is set."""
    return os.path.exists(bypass_flag_path)

def set_bypass_flag():
    """Set the bypass flag."""
    with open(bypass_flag_path, 'w') as f:
        f.write('')

def clear_bypass_flag():
    """Clear the bypass flag."""
    if check_bypass_flag():
        os.remove(bypass_flag_path)


# Path: ShoppingApp/app/data/user_generator.py

