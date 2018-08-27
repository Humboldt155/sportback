from rest_framework import serializers

from sports.models import Sport, SportType, SportGroup, SportSubGroup


class SportSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Sport
        fields = [
            'pk',
            # 'url',
            'ru_name',
            'ru_description',
            'en_name',
            'en_description',
            'sport_sub_groups'
        ]
        # extra_kwargs = {
        #     'url': {
        #         'view_name': 'sports:sport-detail',
        #     }
        # }


class SportGroupSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = SportGroup
        fields = ('url', 'id', 'ru_name', 'ru_description', 'en_name', 'en_description')
        # extra_kwargs = {
        #     'url': {
        #         'view_name': 'sports:sport-detail',
        #     }
        # }


class SportSubGroupSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = SportSubGroup
        fields = ('url', 'id', 'ru_name', 'ru_description', 'en_name', 'en_description')
        # extra_kwargs = {
        #     'url': {
        #         'view_name': 'sports:sport-detail',
        #     }
        # }


class SportTypeSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = SportType
        fields = ('url', 'id', 'ru_name', 'ru_description', 'en_name', 'en_description')
        # extra_kwargs = {
        #     'url': {
        #         'view_name': 'sports:sport-detail',
        #     }
        # }
