from textnode import TextNode, TextType, text_node_to_html_node
import re
from blocktype import block_to_block_type, BlockType
from htmlnode import LeafNode, ParentNode
import os


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            final_nodes.append(old_node)
            continue
        raw_text = old_node.text.split(delimiter)
        if len(raw_text) % 2 == 0:
            raise Exception(f"invalid Markdown Syntax: {old_node.text}")
        for i in range(0,len(raw_text)):
            if i % 2 == 0:
                final_nodes.append(TextNode(raw_text[i], TextType.TEXT))
            elif i % 2 == 1:
                final_nodes.append(TextNode(raw_text[i], text_type))
    return final_nodes
        
def extract_markdown_images(text):
    tuple_of_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return tuple_of_images
    
def extract_markdown_links(text):
    tuple_of_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return tuple_of_links

def split_nodes_image(old_nodes):
    final_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            final_nodes.append(old_node)
            continue
        images_found = extract_markdown_images(old_node.text)
        if len(images_found) < 1:
            final_nodes.append(old_node)
            continue
        new_texts = old_node.text.split(f"![{images_found[0][0]}]({images_found[0][1]})", 1)
        while len(images_found) > 0:
            if new_texts[0] != "":
                final_nodes.append(TextNode(new_texts[0], TextType.TEXT))
            final_nodes.append(TextNode(images_found[0][0], TextType.IMAGE, images_found[0][1]))
            images_found = images_found[1:]
            if len(images_found)>0:
                new_texts = new_texts[1].split(f"![{images_found[0][0]}]({images_found[0][1]})", 1)
        if new_texts[1] != "":
            final_nodes.append(TextNode(new_texts[1], TextType.TEXT))
    return final_nodes

def split_nodes_link(old_nodes):
    final_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            final_nodes.append(old_node)
            continue
        links_found = extract_markdown_links(old_node.text)
        if len(links_found) < 1:
            final_nodes.append(old_node)
            continue
        new_texts = old_node.text.split(f"[{links_found[0][0]}]({links_found[0][1]})", 1)
        while len(links_found) > 0:
            if new_texts[0] != "":
                final_nodes.append(TextNode(new_texts[0], TextType.TEXT))
            final_nodes.append(TextNode(links_found[0][0], TextType.LINK, links_found[0][1]))
            links_found = links_found[1:]
            if len(links_found)>0:
                new_texts = new_texts[1].split(f"[{links_found[0][0]}]({links_found[0][1]})", 1)
        if new_texts[1] != "":
            final_nodes.append(TextNode(new_texts[1], TextType.TEXT))
    return final_nodes

def text_to_textnodes(text):
    nodes = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([nodes], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown):
    markdown = markdown.strip("\n")
    blocks = markdown.split("\n\n")
    final_blocks = []
    for block in blocks:
        block = block.strip("\n")
        block = block.strip(" ")
        if block != "":
            final_blocks.append(block)
    return final_blocks

def markdown_to_html_node(markdown):
    first_borns = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type_of_block = block_to_block_type(block)
        childrens_html = text_to_children(block, type_of_block)
        first_borns.extend(childrens_html)
    return ParentNode("div", first_borns)

def text_to_children(text, type_of_block):
    nodes = []
    if type_of_block == BlockType.HEADING:
        headings = text.split("\n")
        for heading in headings:
            line = heading.split("# ")
            nodes.append(LeafNode(f"{type_of_block.value}{len(line[0]) +1}", line[1]))

    elif type_of_block == BlockType.ORDERED_LIST or type_of_block == BlockType.UNORDERED_LIST:
        lines = text.split("\n")
        parent_node = ParentNode(type_of_block.value, [])
        for line in lines:
            divided_line = line.split(" ", 1)
            text_nodes = text_to_textnodes(divided_line[1])
            childrens_in_leaf = []
            for text_node in text_nodes:
                childrens_in_leaf.append(text_node_to_html_node(text_node))
            nodes.append(ParentNode("li", childrens_in_leaf))            
        nodes.append(parent_node)

    elif type_of_block == BlockType.QUOTE:
        nodes.append(LeafNode(type_of_block.value, text.replace("> ", "")))

    elif type_of_block == BlockType.CODE:
        nodes.append(LeafNode("code", text.replace("```", "")))

    else:
        text_nodes = text_to_textnodes(text)
        childrens_in_leaf = []
        for text_node in text_nodes:
            childrens_in_leaf.append(text_node_to_html_node(text_node))
        nodes.append(ParentNode("p", childrens_in_leaf))
    return nodes
    
def extract_title(markdown):
    markdown = markdown.split("\n\n")
    for i in markdown:
        if i.startswith("# "):
            result = i[1:].strip(" ")
            return result
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", content)
    
    with open(dest_path, "w") as f:
        f.write(final_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)
    for item in items:
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            new_file_path = os.path.join(dest_dir_path, item.replace("md", "html"))
            generate_page(item_path, template_path, new_file_path)
        else:
            new_folder_path = os.path.join(dest_dir_path, item)
            os.mkdir(new_folder_path)
            generate_page_recursive(item_path, template_path, new_folder_path)
