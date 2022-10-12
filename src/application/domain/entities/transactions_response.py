from dataclasses import dataclass

@dataclass
class TransactionsResponse:
    qty_buy_transactions: float
    qty_sell_transactions: float

def diary_balance(list_json) -> float:
    balance = 0

    for i in list_json:
        if i.type == 'BUY':
            balance += i.qty
        if i.type == 'SELL':
            balance += i.qty

    return balance
