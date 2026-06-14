from rest_framework import serializers


class CompetitionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    season = serializers.IntegerField()
