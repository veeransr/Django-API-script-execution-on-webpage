from rest_framework import serializers
from .models import entervaluesAOFT1

class resultSerializer(serializers.ModelSerializer):

    class Meta:
        model = entervaluesAOFT1
        fields = ('number1', 'number2', 'number3')
        # fields = '__all__'