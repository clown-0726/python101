from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from commodity.models import Trolley, Commodity
from user.serializer import UserProfileSerializer


class CommodityEditSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    desc = serializers.CharField(required=False, max_length=1000)
    owner_id = serializers.CharField(required=True, max_length=1000)

    def create(self, validated_data):
        # print(self.context)
        # 通过 context 得到 user
        # user = self.context["request"].user
        # validated_data['owner'] = user
        return Commodity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.save()
        return instance


class CommoditySerializer(serializers.ModelSerializer):
    # 默认返回 owner id，这样覆盖 owner 用实例代替
    owner = UserProfileSerializer()

    class Meta:
        model = Commodity
        fields = '__all__'


class TrolleySerializer(ModelSerializer):
    class Meta:
        model = Trolley
        fields = '__all__'
