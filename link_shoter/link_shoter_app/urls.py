from django.urls import path
from .views import input_link, relink

urlpatterns = [
    path('', input_link, name='input_link'),
    path('<data>', relink)

]
