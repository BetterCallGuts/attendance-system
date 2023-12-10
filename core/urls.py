
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("attend/<int:pk>/",views.attender, name="attend"),
    path("csv/<int:pk>/" , views.import_ex, name='excel'),
    path("attend-grid/<int:pk>/", views.attend_grid, name="attend-grid")
    
]
