from django.urls import include, path
from rest_framework import routers
from project.apps.classifiers.api import (
    ClassifierViewSet,
    PredcitResultsApiView,
    DataFileViewSet,
)

router_data_file = routers.DefaultRouter()
router_data_file.register(r"", DataFileViewSet, basename="DataFile")
urlpatterns = [path("data-csv/", include(router_data_file.urls))]

router_classifier = routers.DefaultRouter()
router_classifier.register(r"", ClassifierViewSet, basename="Classifier")
urlpatterns += [path("classifier/", include(router_classifier.urls))]

urlpatterns += [
    path("predict/", PredcitResultsApiView.as_view()),
]

# urlpatterns += [
#     path("train-model/", ClassifierApiView.as_view()),
# ]
