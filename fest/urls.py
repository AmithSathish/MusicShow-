from django.urls import path
from . import views

urlpatterns = [
    path('',views.page, name="HomePage"),
    path('ticket.html',views.page2,name="tiketpage")
]