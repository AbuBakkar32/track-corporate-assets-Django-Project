from django.contrib import admin
from django.urls import path
import corporateAssetsTracker.views as views
import corporateAssetsTracker.api.views as api

urlpatterns = [
    path('', views.add_company, name='add_company'),
]
