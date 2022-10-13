from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    date: date
    type: str
    qty: float
    price: float
    cost: float
