# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    New_python.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmaghri <mmaghri@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/31 19:10:31 by mmaghri           #+#    #+#              #
#    Updated: 2024/01/31 19:45:31 by mmaghri          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
from difflib import get_close_matches

def load_knowledge_base(file_path : str) -> dict:
    with open(file_path ,'r') as file:
        data: dict = json.load(file)
    return data

# json.dump(), the serialization process 
# converts the Python dictionary into 
# a JSON (JavaScript Object Notation) formatted string:

def  save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)