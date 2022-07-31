from django.urls import path

from .views import TopTemplateView

urlpatterns = [
    path('top', TopTemplateView.as_view(), name='index'),
]
