from dataclasses import dataclass
from typing import Dict

@dataclass
class Document:
    id: str
    text: str
    metadata: Dict