from enum import IntEnum
from typing import Optional

from tortoise.fields import (ForeignKeyField, TextField, CharField,
                             ReverseRelation, CASCADE, IntEnumField, )

from .. import models
from ..models.base import AbstractBaseModel


class QuestionType(IntEnum):
    STRAIGHT = 0
    YES_NO = 1


class Question(AbstractBaseModel):
    class Meta:
        table = "questions"

    text = TextField()
    image: Optional[str] = CharField(max_length=255, null=True)
    test = ForeignKeyField(model_name="models.Test",
                           related_name="questions",
                           on_delete=CASCADE,
                           index=True)
    answers: ReverseRelation["models.Answer"]
    takes: ReverseRelation["models.Take"]
    type: QuestionType = IntEnumField(QuestionType)
