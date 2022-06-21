from django.db.utils import DataError
from django.test import TestCase

from project.apps.classifiers.models import Classifier, DataFile


# pylint: disable=no-member
class TestDataFileModel(TestCase):
    def test_data_file_create_ok(self):
        data_file = DataFile.objects.create(
            file_path="path/to/file.csv", file_name="file.csv"
        )

        self.assertEqual(data_file.file_path, "path/to/file.csv")
        self.assertEqual(data_file.file_name, "file.csv")

    def test_data_file_without_file_name(self):
        data_file = DataFile.objects.create(file_path="path/to/file.csv")

        self.assertEqual(data_file.file_path, "path/to/file.csv")
        self.assertEqual(data_file.file_name, None)

    def test_data_file_without_file_path(self):
        data_file = DataFile.objects.create(file_name="file.csv")

        self.assertEqual(bool(data_file.file_path), False)
        self.assertEqual(data_file.file_name, "file.csv")


class TestClassifierModel(TestCase):
    def setUp(self):
        self.data_file = DataFile.objects.create(
            file_path="path/to/file.csv", file_name="file.csv"
        )
        self.classifier = Classifier.objects.create(
            data_file_name="file.csv",
            test_size=0.25,
            data_file=self.data_file,
            classifier_name="classifier_name",
            accuracy=85,
        )

    def test_classifier_create_ok(self):
        self.assertEqual(self.classifier.data_file_name, "file.csv")
        self.assertEqual(self.classifier.test_size, 0.25)
        self.assertEqual(self.classifier.data_file, self.data_file)
        self.assertEqual(self.classifier.classifier_name, "classifier_name")
        self.assertEqual(self.classifier.accuracy, 85)

    def test_classifier_data_file_name_greater_than_max_len(self):
        self.classifier.data_file_name = "a" * 300
        with self.assertRaises(DataError):
            self.classifier.save()

    def test_classifier_classifier_name_greater_than_max_len(self):
        self.classifier.classifier_name = "a" * 300
        with self.assertRaises(DataError):
            self.classifier.save()
