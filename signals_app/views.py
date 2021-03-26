from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Signals
from .serializers import SignalSerializer
# Create your views here.


class SignalView(ModelViewSet):
      queryset = Signals.objects.all()
      serializer_class = SignalSerializer

