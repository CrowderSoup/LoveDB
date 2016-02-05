from django.db import models


class Reason(models.Model):
    reason_text = models.CharField(max_length=200)
    been_used = models.BooleanField()
    created_date = models.DateTimeField('date created')

    def __str__(self):
        return self.reason_text
