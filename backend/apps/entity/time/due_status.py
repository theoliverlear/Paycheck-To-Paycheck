from enum import Enum


class DueStatus(Enum):
    NOT_DUE: str = 'not due'
    DUE: str = 'due'
    PAST_DUE: str = 'past due'
