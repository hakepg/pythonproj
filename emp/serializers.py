from rest_framework.serializers import ModelSerializer
from .models import employee


# Serializers define the API representation.
class EmpSerializer(ModelSerializer):
        class Meta:
            model = employee
            fields = '__all__'
