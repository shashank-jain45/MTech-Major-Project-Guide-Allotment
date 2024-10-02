from django.urls import path
from .views import *
urlpatterns = [
    path('', upload_csv, name='upload_csv'),
    path('csv-files/', csv_file_list, name='csv_file_list'),
    path('download_csv/<str:file_type>/', download_csv, name='download_csv'),
]
