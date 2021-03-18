from enum import Enum, IntEnum

from tortoise.fields import (CharField, CharEnumField, IntEnumField,
                             BigIntField, ReverseRelation)
from tortoise import Model
from .. import models


class AccessLevel(IntEnum):
    USER = 0
    MODERATOR = 1
    ADMIN = 2


class Status(Enum):
    BLOCKED = "BLOCKED"
    ACTIVE = "ACTIVE"
    DEACTIVATED = "DEACTIVATED"


class Customer(Model):
    id = BigIntField(pk=True)
    name = CharField(max_length=255, null=True)
    name_again = CharField(max_length=255, null=True)
    username = CharField(max_length=32, null=True)
    language = CharField(max_length=8, null=True)
    status = CharEnumField(Status, default=Status.ACTIVE, index=True)
    access = IntEnumField(AccessLevel, default=AccessLevel.USER)
    takes: ReverseRelation["models.Take"]

    class Meta:
        table = "customers"
        table_description = 'All users who have ever started the bot'

    def __str__(self):
        return f"{self.id}:{self.name}"
