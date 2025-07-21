
from typing import Dict

def add(a: int, b: int) -> int:
    return a + b

d = {"a": 5, "6": 7}

def empty(d: Dict[str, int]):
    print(d)
    del d["a"]

print(d)
empty(d)
print(d)

#mypy detects type errors