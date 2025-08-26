from copy_static import *
from generate_page import *
import sys

from_path = "content/"
template_path = "template.html"
dest_path = "docs/"

basepath = sys.argv[1] or "/"

def main():
    copy_static(dest_path)
    generate_pages_recursive(from_path, template_path, dest_path, basepath)

main()