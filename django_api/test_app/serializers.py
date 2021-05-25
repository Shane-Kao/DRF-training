from rest_framework import serializers

from .models import TestModel

class SimpleObject:
    def __init__(self, name):
        self.name = name


class SimpleObjectSerializer(serializers.Serializer):
    name = serializers.CharField()


def run_data():
    simple_var = SimpleObject(name="Henry")
    simple_var_serializer = SimpleObjectSerializer(simple_var)
    print(simple_var_serializer.data)


class SimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    phone_number = serializers.IntegerField()
    is_live = serializers.BooleanField()
    amount = serializers.FloatField()
    extra_name = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return TestModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        TestModel.objects.filter(id=instance.id).update(**validated_data)
        return TestModel.objects.get(id=instance.id)
# run_data()