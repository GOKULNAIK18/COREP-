from dataclasses import dataclass
from typing import List

@dataclass
class CorepField:
    row: str
    description: str
    amount: float
    rule_reference: str

@dataclass
class CorepReport:
    template: str
    fields: List[CorepField]
