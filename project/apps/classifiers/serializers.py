from rest_framework import serializers

from project.apps.classifiers.models import DataFile, Classifier, DataFileHeader


class DataFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataFile
        fields = "__all__"


class ClassifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classifier
        fields = "__all__"


class DataFileHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataFileHeader
        fields = "__all__"
