from dataclasses import dataclass


@dataclass
class TransactionResponse:
    buy_qty: int
    sell_qty: int

    def __repr__(self) -> str:
        return f'Total BUY: {self.buy_qty}/ Total SELL: {self.sell_qty}'
