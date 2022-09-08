from django.contrib.auth.models import User, Group
from rest_framework import serializers

from mainapp.models import ExampleModel


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'


# class SalModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class SalSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length = 255)
#     content = serializers.CharField()


# def encode():
#     model = ExampleModel
#     model_sr = SalSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
