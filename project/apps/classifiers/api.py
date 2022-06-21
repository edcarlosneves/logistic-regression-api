from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# pylint: disable=duplicate-code
from project.apps.classifiers.models import (
    Classifier,
    DataFile,
    DataFileHeader,
    Prediction,
)
from project.apps.classifiers.serializers import (
    ClassifierSerializer,
    DataFileHeaderSerializer,
    DataFileSerializer,
    PredictionSerializer,
)
from project.apps.classifiers.utils import PredictResults, TrainModel
from project.commons.utils import get_headers_from_csv, get_timenow_str


# pylint: disable=too-many-ancestors, no-member
class ClassifierViewSet(viewsets.ModelViewSet):
    serializer_class = ClassifierSerializer
    queryset = Classifier.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        data_file_name = self.request.data["data_file_name"]
        test_size = self.request.data["test_size"]
        train_model = TrainModel(data_file_name=data_file_name, test_size=test_size)
        classifier_accuracy, classifier_name = train_model()
        data_file = DataFile.objects.get(file_name=data_file_name)
        serializer.save(
            accuracy=classifier_accuracy,
            classifier_name=classifier_name,
            data_file=data_file,
        )


class PredcitResultsApiView(APIView):
    # pylint: disable=no-self-use
    def post(self, request):
        classifier_name = request.data["classifier_name"]
        input_data = request.data["input_data"]
        predictor = PredictResults(classifier_name=classifier_name)
        result = predictor.predict_result(input_data)
        is_purchased = result[0]
        return Response({"result": is_purchased}, status=status.HTTP_200_OK)


class DataFileViewSet(viewsets.ModelViewSet):
    serializer_class = DataFileSerializer
    queryset = DataFile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "success"}, status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        timestr = get_timenow_str()
        data_file_name = self.request.data["file_path"].name
        data_file_name_without_extension = data_file_name.split(".")[0]
        new_data_file_name = f"{data_file_name_without_extension}_{timestr}.csv"
        self.request.data["file_path"].name = new_data_file_name
        saved_serializer = serializer.save(file_name=new_data_file_name)
        data_file_headers = get_headers_from_csv(new_data_file_name)
        for data_file_header in data_file_headers:
            DataFileHeader.objects.create(
                data_file=saved_serializer, header_name=data_file_header
            )
        return saved_serializer


class DatafileHeaderViewSet(viewsets.ModelViewSet):
    serializer_class = DataFileHeaderSerializer
    queryset = DataFileHeader.objects.all()


class PredictionViewSet(viewsets.ModelViewSet):
    serializer_class = PredictionSerializer
    queryset = Prediction.objects.all()
