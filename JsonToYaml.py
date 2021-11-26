# convert json list to yaml

"""
psuedo code: 
    - get json file
    - get first index of json array 
    - extract all the keys 
    - use a for loop to extract data from list using the keys obtained
    - write array to md file 
"""
import json

# get json file and convert to python dict array
with open("./array.json", encoding="utf8") as json_array:
    dict_array = json.load(json_array)


# get all the keys from the dictionary
# all the objects in array must be of the same shape for this to work
keys = list(dict_array[0].keys())

# File info --- change to whatever you want
file_title = "Menu"
data_title = "menu_item"
file_body = "This is the menu page for the Flamingo Restaurant Website"


toml_string = f"""
title: {file_title}
{data_title}:
"""
for json_object in dict_array:
    current = ""
    first = True
    for key in keys:
        data = json_object[key]
        if len(data) <= 0:
            data = '""'
        if first:
            current += f"\t- {key}: {data}\n"
            first = False
            continue
        current += f"\t  {key}: {data}\n"
    toml_string += current


# format the md file
toml_string = f"""
---
{toml_string}
---
{file_body}
""".strip()

# write to md file
with open(f"./{file_title.lower()}.md", "w", encoding="utf8") as markdown:
    markdown.writelines(toml_string)
