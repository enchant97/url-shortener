from tortoise.fields.data import CharField, DatetimeField
from tortoise.models import Model


class Url(Model):
    short_id = CharField(max_length=8, pk=True)
    url = CharField(1500, unique=True)
    created_at = DatetimeField(auto_now_add=True)

    class Meta:
        table = "urls"
