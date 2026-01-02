from textnode import TextNode, TextType
import re


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
        number_of_images = len(images_found)
        new_texts = old_node.text.split(f"![{images_found[0][0]}]({images_found[0][1]})", 1)
        while number_of_images > 0:
            if new_texts[0] != "":
                final_nodes.append(TextNode(new_texts[0], TextType.TEXT))
            final_nodes.append(TextNode(images_found[0][0], TextType.IMAGE, images_found[0][1]))
            number_of_images -= 1
            images_found = extract_markdown_images(new_texts[1])
            if len(images_found)>0:
                new_texts = new_texts[1].split(f"![{images_found[0][0]}]({images_found[0][1]})", 1)
    if new_texts[1] != "":
        final_nodes.append(TextNode(new_texts[1], TextType.TEXT))
    return final_nodes
