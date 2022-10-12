from ast import List
from src.application.input import read_json
from src.application.domain.transactions import Transaction


def make_transaction_list() -> list:
    date_list = read_json("transactions.json")
    transaction_list: List[Transaction] = []
    for i in date_list:
        transaction_list.append(Transaction(**i))
    return transaction_list

def calculate_daily_balance():