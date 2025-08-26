import shutil
import os

public_path = "public/"
static_path = "static/"

def copy_static():
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
        os.mkdir(public_path)

    copy_recursive(static_path, public_path)

def copy_recursive(from_path, to_path):
    from_dir_ls = os.listdir(from_path)
    for i in from_dir_ls:
        path = os.path.join(from_path, i)
        if os.path.isdir(path):
            to_dir = os.path.join(to_path, i)
            if not os.path.exists(to_dir):
                os.mkdir(to_dir)
            copy_recursive(path, to_dir)
        else:
            shutil.copy(path, to_path)