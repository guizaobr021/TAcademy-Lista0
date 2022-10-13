from ast import List
from datetime import date
import json
from src.application.domain.entities.transaction_response import TransactionResponse
from src.application.domain.entities.balance_response import BalanceResponse
from src.application.domain.transactions import Transaction
from src.application.input import read_json


def make_transaction_list() -> list:
    date_list = read_json("transactions.json")
    transaction_list: List[Transaction] = []
    for i in date_list:
        transaction_list.append(Transaction(**i))
    return transaction_list

def calculate_total_transactions(transaction_list: Transaction) -> float:
    buy_qty = 0
    sell_qty = 0
    for i in transaction_list:
        if i.type == 'BUY':
            buy_qty += i.qty
        if i.type == 'SELL':
            sell_qty += i.qty

    return TransactionResponse(buy_qty, sell_qty)

def calculate_daily_balance(transaction_list: Transaction) -> float:
    previous_date = transaction_list[0].date
    daily_list: List[BalanceResponse] =[]
    balance = 0

    for i in transaction_list:
        if i.date != previous_date:
            daily_list.append(BalanceResponse(i.date, balance))
            previous_date = i.date

        if i.type == 'BUY':
            balance += i.qty
        else:
            balance -= i.qty
    daily_list.append(BalanceResponse(i.date, balance))

    return daily_list

def calculate_days_diference(transaction_list: Transaction) -> int:
    smallest_date = date(2080, 1, 1)
    biggest_date = transaction_list[0].date

    for i in transaction_list:
        if i.date < smallest_date:
            smallest_date = i.date
        elif i.date > biggest_date:
            biggest_date = i.date

    return biggest_date.toordinal() - smallest_date.toordinal()

def generate_balance_json(transaction_list: List) -> None:
    with open("balance.json", "w", encoding='utf8') as arquivo:
        json.dump([i.__dict__ for i in transaction_list], arquivo, default=str, indent=None)
