from django.urls import path
from treding import views
urlpatterns = [
    path('',views.index,name="index"),
]
