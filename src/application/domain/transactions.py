from dataclasses import dataclass
import datetime

@dataclass
class Transaction:
    date: datetime
    type: str
    qty: float
    price: float
    cost: float
