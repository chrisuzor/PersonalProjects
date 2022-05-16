import random
import string
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass()
class Person:
    name: str
    address: str
    email: str
    active: bool = True
    # email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    search_string: str = field(init=False)

    def __post_init__(self) -> None:
        self.search_string = f"{self.name} {self.address}"

    def __str__(self):
        return f"{self.name}, {self.address} {self.email}"


print(Person("Chris", "Abuja", "Email"))


class Role(Enum):
    """Employee Roles"""

    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()
