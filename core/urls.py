from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),  #  Home page
    path('generate/', index, name="index"),  #  Main logic page
    path('get-intents/', get_intents, name="get_intents"),

]