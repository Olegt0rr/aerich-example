from tortoise import Model
from tortoise.fields import IntField, CharField


class User(Model):
    id = IntField(pk=True)
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
