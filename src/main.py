import os
import shutil
from functions import extract_title, generate_page, generate_page_recursive
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    

    project_path = os.path.abspath("")
    static_path = os.path.join(project_path, "static")
    #public_path = os.path.join(project_path, "public") # Deleted after the completion of the project
    docs_directory = os.path.join(project_path, "docs")

    template_path = os.path.join(project_path, "template.html")
    content_path = os.path.join(project_path, "content")
    
    copy_to_dic(static_path, docs_directory)
    generate_page_recursive(content_path, template_path, docs_directory, basepath)

#this function overwrites/create the "dest" folder
def copy_to_dic(origin, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    items = os.listdir(origin)
    for item in items:
        item_path = os.path.join(origin, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest)
        else:
            dic_path = os.path.join(dest, item)
            copy_to_dic(item_path, dic_path)
    
    


main()