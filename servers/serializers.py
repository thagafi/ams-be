from rest_framework import serializers
from computers.models import CPUModel, RamSize, MonitorSize, OS, Brand
from users.serializers import UserSerializer
from users.models import User
from .models import ServersModel

class UserRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return UserSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class ServerSerializer(serializers.ModelSerializer):
    user = UserRelatedField(many=False, queryset=User.objects.all())

    class Meta:
        model = ServersModel
        fields = "__all__"