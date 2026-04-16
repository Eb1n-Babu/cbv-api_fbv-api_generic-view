from rest_framework import serializers

from views.models import Customer

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'