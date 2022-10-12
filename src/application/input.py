import json

def read_json(json_file) -> list:
    with open(json_file, encoding='utf-8') as data_json:
        json_list = []
        opened_json = json.load(data_json)
        for line in opened_json:
            json_list.append(line)
    return json_list
