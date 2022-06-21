from django.urls import include, path

from rest_framework import routers

from project.apps.classifiers.api import (
    ClassifierViewSet,
    DatafileHeaderViewSet,
    DataFileViewSet,
    PredcitResultsApiView,
    PredictionViewSet,
)

router = routers.DefaultRouter()
router.register("data-csv", DataFileViewSet, basename="DataFile")
router.register("data-csv-header", DatafileHeaderViewSet, basename="DatafileHeader")
router.register("classifier", ClassifierViewSet, basename="Classifier")
router.register("prediction", PredictionViewSet, basename="Prediction")

urlpatterns = [
    path("", include(router.urls)),
    path("predict/", PredcitResultsApiView.as_view()),
]
