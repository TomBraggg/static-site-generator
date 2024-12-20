import os
import shutil
from mdconvert.htmlnode_utility import markdown_to_html_str, extract_title


static_path = "static"
public_path = "public"

def start() -> None:
    _wipe_public()
    _copy_dir_to_target(static_path, public_path)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path) -> None:
    nodes = os.listdir(dir_path_content)
    for node in nodes:
        current_path = f"{dir_path_content}/{node}"
        if not os.path.isdir(current_path):
            _generate_page(current_path, template_path, dest_dir_path)
        else:
            os.path.join(dir_path_content, node)
            target = f"{dest_dir_path}/{node}"
            os.mkdir(target)
            generate_page_recursive(current_path, template_path, target)

def _wipe_public() -> None:
    if public_path in os.listdir():
        shutil.rmtree(public_path)
    os.path.join(public_path)
    os.mkdir(public_path)

def _copy_dir_to_target(source: str, target: str) -> None:
    nodes = os.listdir(source)
    for node in nodes:
        current_path = f"{source}/{node}"
        if not os.path.isdir(current_path):
            shutil.copy(current_path, target)
        else:
            os.path.join(target, node)
            target = f"{target}/{node}"
            os.mkdir(target)
            _copy_dir_to_target(current_path, target)

def _generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"""
Generating page...
From path: {from_path}
Template path: {template_path}
Destination_path: {dest_path}
          """)
    with open(from_path, "r") as content_path:
        content_md = content_path.read()
    with open(template_path, "r") as template_path:
        html_template = template_path.read()
    content = markdown_to_html_str(content_md)
    title = extract_title(content_md)
    html = html_template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    html_path = os.path.join(dest_path, "index.html")
    with open(html_path, "w") as file:
        file.write(html)

_wipe_public()