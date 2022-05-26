from django.db import models


class DataFile(models.Model):
    file_path = models.FileField(upload_to="files/data-files")
    file_name = models.CharField(max_length=60, null=True)

    class Meta:
        db_table = "classifiers_data_file"
        verbose_name_plural = "Data Files"

    def __str__(self):
        return f"{self.file_name}"


class DataFileHeader(models.Model):
    data_file = models.ForeignKey(
        DataFile, on_delete=models.CASCADE, null=True, blank=True
    )
    header_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "classifiers_data_file_header"
        verbose_name_plural = "Data File Headers"

    def __str__(self):
        return f"{self.data_file} -> {self.header_name}"


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


class Prediction(models.Model):
    classifier = models.ForeignKey(Classifier, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Predictions"

    def __str__(self):
        return f"Classifier used: {str(self.classifier)}"


class PredictionInputData(models.Model):
    input_data = models.FloatField()
    input_label = models.CharField(max_length=255)
    data_file_header = models.ForeignKey(DataFileHeader, on_delete=models.CASCADE)
    prediction = models.ForeignKey(
        Prediction,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "classifiers_prediction_input_data"
        verbose_name_plural = "Predctions Input Data"

    def __str__(self):
        return f"{self.input_label}: {self.input_data}"
