from tortoise.fields import (CharField, ForeignKeyField, BooleanField,
                             ReverseRelation, CASCADE, )

from .. import models
from ..models.base import AbstractBaseModel


class Test(AbstractBaseModel):
    class Meta:
        table = "tests"

    name = CharField(max_length=255)
    group = ForeignKeyField(model_name="models.Group",
                            related_name="tests",
                            on_delete=CASCADE,
                            index=True)
    is_enabled = BooleanField(default=True)
    questions: ReverseRelation["models.Question"]
    takes: ReverseRelation["models.Take"]
