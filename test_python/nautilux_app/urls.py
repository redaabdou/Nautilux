from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('equipment/', views.EquipmentList.as_view()),
    path('equipment/<int:pk>/', views.EquipmentDetail.as_view()),
    path('categories/', views.CategoriesList.as_view()),
    path('equipments/', views.EquipmentsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)