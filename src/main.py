import os
import shutil
from functions import extract_title, generate_page

def main():
    project_path = os.path.abspath("")
    static_path = os.path.join(project_path, "static")
    public_path = os.path.join(project_path, "public")
    content_path = os.path.join(project_path, "content/index.md")
    template_path = os.path.join(project_path, "template.html")
    dest_path = os.path.join(project_path, "public/index.html")
    copy_to_dic(static_path, public_path)
    generate_page(content_path, template_path, dest_path)

#this function overwrites/create the "dest" folder
def copy_to_dic(origin, dest):
    if os.path.exists(dest):
        delete_dir(dest)
    os.mkdir(dest)
    items = os.listdir(origin)
    for item in items:
        item_path = os.path.join(origin, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest)
        else:
            dic_path = os.path.join(dest, item)
            copy_to_dic(item_path, dic_path)
    
def delete_dir(path):
    shutil.rmtree(path)


main()