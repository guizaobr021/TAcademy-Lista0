from dataclasses import dataclass

@dataclass
class TransactionsResponse:
    qty_buy_transactions: float
    qty_sell_transactions: float

def total_transactions(list_json) -> list:
    buy_qty = 0
    sell_qty = 0

    for i in list_json:
        if i.type == 'BUY':
            buy_qty += i.qty
        if i.type == 'SELL':
            sell_qty += i.qty

    return TransactionsResponse(buy_qty, sell_qty)
