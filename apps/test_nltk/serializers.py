from rest_framework import serializers

class SynonymSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)
    synonyms = serializers.ListField(child=serializers.CharField())

class AntonymSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)
    antonyms = serializers.ListField(child=serializers.CharField())
