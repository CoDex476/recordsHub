from django.db import models
from django.contrib.auth.models import User

def upload_to_memo(instance, filename):
    return f'memos/{instance.user.id}/{filename}'


def upload_to_receipt(instance, filename):
    return f'receipts/{instance.user.id}/{filename}'

class Memo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    memo_file = models.FileField(upload_to=upload_to_memo)
    created_at = models.DateTimeField(auto_now_add=True)

class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    receipt_file = models.FileField(upload_to=upload_to_receipt)
    created_at = models.DateTimeField(auto_now_add=True)
