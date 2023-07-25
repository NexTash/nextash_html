import os

def if_file_exist(path):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_folder, "public/pages", f"{path}.html")
    
    if os.path.exists(full_path):
        return True
    else:
        return False