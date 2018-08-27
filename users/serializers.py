# from rest_framework import serializers
#
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
# class UserSerializer(serializers.ModelSerializer):
#     # sports = serializers.HyperlinkedRelatedField(
#     #     many=True,
#     #     view_name='sports:sport-detail',
#     #     read_only=True
#     # )
#     date_joined = serializers.ReadOnlyField()
#
#     # def update(self, instance, validated_data):
#     #     for field in validated_data:
#     #         if field == 'password':
#     #             instance.set_password(validated_data.get(field))
#     #         else:
#     #             instance.__setattr__(field, validated_data.get(field))
#     #     instance.save()
#     #     return instance
#
#     class Meta:
#         model = User
#         fields = ('id', 'password', 'name', 'refused_newsletters',
#                   'email'
#                   )


from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'name', 'refused_newsletters',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}
