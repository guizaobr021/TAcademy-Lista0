import json
from src.application.domain.transactions import Transaction

def received_json() -> list:
    transaction_list = []
    with open('transactions.json', encoding='utf-8') as data_json:
        opened_json = json.loads(data_json)
        for line in opened_json:
            transaction_list.append(Transaction(**line))
    return transaction_list
