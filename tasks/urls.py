from django.urls import path
from . import views


urlpatterns = [
    path('' , views.getTasks),
    path('<int:id>/', views.getById)
]