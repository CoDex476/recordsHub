from django.shortcuts import render

from rest_framework import generics
from .models import Memo, Receipt
from .serializers import MemoSerializer, ReceiptSerializer

class MemoListCreateView(generics.ListCreateAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReceiptListCreateView(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
