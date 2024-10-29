import os
import shutil

static_path = "./static"
public_path = "./public"

def start():
    wipe_public()
    copy_dir_to_target(static_path, public_path)

def copy_dir_to_target(source: str, target: str):
    nodes = os.listdir(source)
    for node in nodes:
        current_path = f"{source}/{node}"
        target = f"{target}"
        if not os.path.isdir(current_path):
            shutil.copy(current_path, target)
        else:
            os.path.join(target, node)
            target = f"{target}/{node}"
            os.mkdir(target)
            copy_dir_to_target(current_path, target)

def wipe_public():
    shutil.rmtree(public_path)
    os.path.join("./", "public")
    os.mkdir(public_path)

start()
