from typing import Optional

from tortoise.fields import (ForeignKeyField, TextField, BooleanField, CASCADE,
                             ReverseRelation, CharField)

from .. import models
from ..models.base import AbstractBaseModel


class Answer(AbstractBaseModel):
    class Meta:
        table = "answers"

    name = CharField(max_length=64, description="displayed before choosing")
    description = TextField(null=True, description="displayed after choosing")
    is_correct: Optional[bool] = BooleanField(null=True)  # type: ignore
    question = ForeignKeyField(model_name="models.Question",
                               related_name="answers",
                               on_delete=CASCADE,
                               index=True)
    takes: ReverseRelation["models.Take"]
