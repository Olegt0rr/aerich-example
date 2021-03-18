from tortoise.fields import (ForeignKeyField, CASCADE, DatetimeField)

from ..models.base import AbstractBaseModel


class Take(AbstractBaseModel):
    class Meta:
        table = "takes"

    created_at = DatetimeField(auto_now_add=True)
    customer = ForeignKeyField(model_name="models.Customer",
                               related_name="takes",
                               on_delete=CASCADE,
                               index=True)
    test = ForeignKeyField(model_name="models.Test",
                           related_name="takes",
                           on_delete=CASCADE,
                           index=True)
    question = ForeignKeyField(model_name="models.Question",
                               related_name="takes",
                               on_delete=CASCADE,
                               index=True)
    answer = ForeignKeyField(model_name="models.Answer",
                             related_name="takes",
                             on_delete=CASCADE,
                             index=True)
