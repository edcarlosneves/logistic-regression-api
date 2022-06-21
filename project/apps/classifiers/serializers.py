from rest_framework import serializers

# pylint: disable=duplicate-code
from project.apps.classifiers.models import (
    Classifier,
    DataFile,
    DataFileHeader,
    Prediction,
)


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


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = "__all__"
