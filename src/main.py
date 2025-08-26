from copy_static import *
from generate_page import *

from_path = "content"
template_path = "template.html"
dest_path = "public"

def main():
    copy_static()
    generate_pages_recursive(from_path, template_path, dest_path)


main()