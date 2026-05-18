import sys, os

def find_executable(cmd_name):
    """Search PATH for an executable. Returns full path or None."""
    path_val = os.environ.get('PATH', '')
    
    for folder in path_val.split(os.pathsep):
        # Linux/Mac: check exact filename
        full_path = os.path.join(folder, cmd_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
        
        # Windows: also check with extensions
        if sys.platform == "win32":
            for ext in ['.exe', '.bat', '.cmd', '.com']:
                full_path_ext = os.path.join(folder, cmd_name + ext)
                if os.path.isfile(full_path_ext):
                    return full_path_ext
    
    return None