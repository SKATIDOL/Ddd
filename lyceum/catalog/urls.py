from django.urls import path, re_path

from . import views
urlpatterns = [
    path('', views.item_list),
    path('<int:pk>/', views.item_detail)
    re_path(r'^re/(?P<a>[1-9][0-9]*)/', views.item)
]
