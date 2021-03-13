from rest_framework import serializers
from .models import Wings, Squads
from users.models import User
from users.serializers import UserSerializer


class UserRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return UserSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)

class WingSerializer(serializers.ModelSerializer):
    wing_commander = UserRelatedField(many=False, queryset=User.objects.all())
    wing_coordinator = UserRelatedField(many=False, queryset=User.objects.all())

    class Meta:
        model = Wings
        fields = ['id', 'wing_name','wing_commander', 'wing_coordinator']


class WingRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return WingSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)




class SquadronSerializer(serializers.ModelSerializer):
    wing = WingRelatedField(many=False, queryset=Wings.objects.all())
    Squad_commander = UserRelatedField(many=False, queryset=User.objects.all())
    Squad_coordinator = UserRelatedField(many=False, queryset=User.objects.all())

    class Meta:
        model = Squads
        fields = ['id', 'Squad_name','wing', 'Squad_commander', 'Squad_coordinator']







