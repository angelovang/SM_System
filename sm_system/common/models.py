from django.db import models

DEVICE = (
    ('computer', 'Computer'),
    ('laptop', 'Laptop'),
    ('monitor', 'Monitor'),
    ('printer', 'Printer')
)


class ServiceInfo(models.Model):
    DEVICE_MAX_LENGTH = 20
    DESCRIPTION_MAX_LENGTH = 200
    PRICE_MAX_LENGTH = 20

    device = models.CharField(
        max_length=DEVICE_MAX_LENGTH,
        choices=DEVICE,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=DESCRIPTION_MAX_LENGTH,
        null=False,
        blank=False,
    )

    price = models.FloatField(
        default= 0.00,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.id}--{self.device}--{self.description}--{self.price}'