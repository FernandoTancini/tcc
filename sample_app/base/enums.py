from enum import Enum as PyEnum

class BaseEnum(PyEnum):
    @classmethod
    def to_choices(cls):
        return [(tag.name, tag.value) for tag in cls]

class ReactionKind(BaseEnum):
    LIKE = 'LIKE'
    LOVE = 'LOVE'
    HATE = 'HATE'