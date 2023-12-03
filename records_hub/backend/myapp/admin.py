from django.contrib import admin

from .models import Memo
from .models import Receipt

class MemoAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "content", "created_at")


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("user", "type", "amount", "date", "receipt_file", "created_at")


#Register model

admin.site.register(Memo, MemoAdmin)
admin.site.register(Receipt, ReceiptAdmin)