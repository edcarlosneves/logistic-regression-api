from django.contrib import admin

from project.apps.classifiers.models import (
    Classifier,
    DataFile,
    DataFileHeader,
    Prediction,
    PredictionInputData,
)


@admin.register(DataFile)
class DataFileAdmin(admin.ModelAdmin):
    pass


@admin.register(Classifier)
class ClassifierAdmin(admin.ModelAdmin):
    pass


@admin.register(DataFileHeader)
class DataFileHeaderAdmin(admin.ModelAdmin):
    pass


@admin.register(Prediction)
class PredctionAdmin(admin.ModelAdmin):
    pass


@admin.register(PredictionInputData)
class PredctionInputDataAdmin(admin.ModelAdmin):
    pass
