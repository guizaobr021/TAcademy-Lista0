import json
import datetime as dt

def read_json(json_file) -> list:
    with open(json_file, encoding='utf-8') as data_json:
        opened_json = json.load(data_json)
        json_list = []
        for line in opened_json:
            line["date"] = dt.datetime.strptime(line["date"],'%Y-%m-%d').date()
            json_list.append(line)
    return json_list
