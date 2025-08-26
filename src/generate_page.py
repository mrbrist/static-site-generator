from markdown_to_html_node import *
from extract_title import *
import os

def generate_page(from_path, template_path, dest_path, basepath):
    from_file = open(from_path).read()
    template_file = open(template_path).read()
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_html = markdown_to_html_node(from_file).to_html()
    title = extract_title(from_file)

    html = template_file.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", from_html)
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    with open(dest_path, "w") as f:
        f.write(html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    from_dir_ls = os.listdir(dir_path_content)
    for i in from_dir_ls:
        path = os.path.join(dir_path_content, i)
        if os.path.isdir(path):
            to_dir = os.path.join(dest_dir_path, i)
            if not os.path.exists(to_dir):
                os.mkdir(to_dir)
            generate_pages_recursive(path, template_path, to_dir, basepath)
        else:
            generate_page(path, template_path, os.path.join(dest_dir_path, i.replace(".md", ".html")), basepath)