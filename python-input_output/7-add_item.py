#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""

import sys
from os.path import exists
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

#Yoxla: fayl movcuddursa< movcud siyahini oxu, eks halda bos siyahi ile basla
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

#Elave olunan arqumentleri siyahiya elave et
items.extend(sys.argv[1:]

#Yenilenmis siyahini fayla yaz
save_to_json_file(items, filename)
