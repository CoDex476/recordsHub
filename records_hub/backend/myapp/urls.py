# myapp/urls.py
from django.urls import path
from .views import MemoListCreateView, ReceiptListCreateView

urlpatterns = [
    path('memos/', MemoListCreateView.as_view(), name='memo-list-create'),
    path('receipts/', ReceiptListCreateView.as_view(), name='receipt-list-create'),
]
