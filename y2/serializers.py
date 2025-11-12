from rest_framework import serializers

from y2.models import Student , Customer


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'