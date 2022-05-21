from django.contrib import admin
from project.apps.classifiers.models import DataFile, Classifier, DataFileHeader


@admin.register(DataFile)
class DataFileAdmin(admin.ModelAdmin):
    pass


@admin.register(Classifier)
class ClassifierAdmin(admin.ModelAdmin):
    pass


@admin.register(DataFileHeader)
class DataFileHeaderAdmin(admin.ModelAdmin):
    pass
