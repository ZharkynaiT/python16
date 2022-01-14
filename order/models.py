from django.contrib.auth.models import User
from django.db import models
from model_utils.fields import StatusField

from product.models import CreatedAtModel
from model_utils import Choices


class Order(CreatedAtModel):
    STATUS = Choices('In progress', 'Canceled', 'Finished')
    total_sum = models.DecimalField(max_length=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='orders')
    product = models.ManyToManyField('product.Product')
    order_status = StatusField()

    class Meta:
        ordering = ['-created_at']
        db_table = 'order'

    def __str__(self):
        return f'Заказ №{self.id} от {self.created_at.strftime("%d-%m-%Y %H:%M")}'
