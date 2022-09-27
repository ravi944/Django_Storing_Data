from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('all_emp/',views.all_emp),
    path('add_emp/',views.add_emp),
    path('delete_emp/<int:id>/',views.delete_emp),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    ]