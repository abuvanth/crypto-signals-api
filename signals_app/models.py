from django.db import models

# Create your models here.


class Signals(models.Model):
    crypto_symbol = models.CharField(max_length=10)
    buy_zone = models.TextField()
    sell_zone = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.crypto_symbol

    class Meta:
        verbose_name_plural = "signals"
