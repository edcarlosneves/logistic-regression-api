from django.urls import include, path
from rest_framework import routers
from project.apps.classifiers.api import (
    ClassifierViewSet,
    PredcitResultsApiView,
    DataFileViewSet,
    DatafileHeaderViewSet,
)

router_data_file = routers.DefaultRouter()
router_data_file.register(r"", DataFileViewSet, basename="DataFile")
urlpatterns = [path("data-csv/", include(router_data_file.urls))]

router_data_file_header = routers.DefaultRouter()
router_data_file_header.register(r"", DatafileHeaderViewSet, basename="DatafileHeader")
urlpatterns += [path("data-csv-header/", include(router_data_file_header.urls))]

router_classifier = routers.DefaultRouter()
router_classifier.register(r"", ClassifierViewSet, basename="Classifier")
urlpatterns += [path("classifier/", include(router_classifier.urls))]

urlpatterns += [
    path("predict/", PredcitResultsApiView.as_view()),
]
