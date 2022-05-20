from django.contrib import admin
from project.apps.classifiers.models import DataFile, Classifier


@admin.register(DataFile)
class DataFileAdmin(admin.ModelAdmin):
    pass


@admin.register(Classifier)
class ClassifierAdmin(admin.ModelAdmin):
    pass
