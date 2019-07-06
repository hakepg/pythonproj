from django.shortcuts import render
from .models import employee
from .serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


# ViewSets define the view behavior.

class EmpViewSet(ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = ModelSerializer

# Create your views here.
