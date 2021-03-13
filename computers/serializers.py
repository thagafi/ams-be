from rest_framework import serializers
from .models import ComputersModel, CPUModel, RamSize, MonitorSize, OS, Brand
from formations.serializers import SquadronSerializer
from users.serializers import UserSerializer
from users.models import User

class UserRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return UserSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class SquadRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return SquadronSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)
        
class ComputerSerializer(serializers.ModelSerializer):
    user = UserRelatedField(many=False, queryset=User.objects.all())
    squad = SquadRelatedField(many=False, queryset=User.objects.all())

    class Meta:
        model = ComputersModel
        fields = "__all__"

class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUModel
        fields = "__all__"


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamSize
        fields = "__all__"


class MonitorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = MonitorSize
        fields = "__all__"

class OSSerializer(serializers.ModelSerializer):
    class Meta:
        model = OS
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"