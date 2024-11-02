import secrets 
from math import log2
from enum import IntEnum

class StrenthToEntropy(IntEnum):
    Слабый = 0
    Ненадёжный = 40
    Средний = 70
    Сильный = 100
    Божественный = 140



def create_new(length: int, characters: str) -> str:
    return ''.join(secrets.choice(characters) for _ in range(length))

def get_entropy(length:int, characters_number: int) -> float:
    try:
        entropy = length * log2(characters_number)
    except ValueError:
        return 0.0

    return round(entropy,2)