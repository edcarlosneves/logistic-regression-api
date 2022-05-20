from django.db import models


class DataFile(models.Model):
    file_path = models.FileField(upload_to="files/data-files")
    file_name = models.CharField(max_length=60, null=True)

    class Meta:
        verbose_name_plural = "Data Files"

    def __str__(self):
        return f"{self.file_name}"


class Classifier(models.Model):
    data_file_name = models.CharField(max_length=255, null=True, blank=True)
    test_size = models.FloatField(null=True, blank=True)
    data_file = models.ForeignKey(
        DataFile, on_delete=models.CASCADE, null=True, blank=True
    )
    classifier_name = models.CharField(max_length=255, null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Classifiers"

    def __str__(self):
        return f"name -> {self.classifier_name} | acc -> {self.accuracy}"
