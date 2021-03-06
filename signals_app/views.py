from rest_framework.viewsets import ModelViewSet
from .models import Signals
from .serializers import SignalSerializer


# Create your views here.


class SignalView(ModelViewSet):
      queryset = Signals.objects.all().order_by('-id')
      serializer_class = SignalSerializer

