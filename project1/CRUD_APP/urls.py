from django.urls import path
from . import views

urlpatterns = [
    path('ov/', views.orderview, name='orderform_url'),
    path('sv/',views.showview, name='showorder_url'),
    path('up/<int:id>/', views.updateview, name='updateorder_url'),
    path('dl/<int:id>/', views.deleteview, name='deleteorder_url')
]