from dataclasses import dataclass
from datetime import date

@dataclass
class BalanceResponse:
    date: date
    balance: float

    def __repr__(self) -> str:
        return f'Daily balance: {self.date} => {self.balance}'
