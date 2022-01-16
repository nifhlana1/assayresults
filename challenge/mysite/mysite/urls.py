"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

#Below are the different endpoints I have created
urlpatterns = [
    re_path('admin/', admin.site.urls),
    #This endpoint returns all of the compounds available (just their codes for use in dropdowns etc at frontent)
    #When running the server, you can test it with this url: http://127.0.0.1:8000/allcompounds/
    re_path('allcompounds/', views.all_compoundsView, name="allcompoundsView"),

    #This endpoint would return compound details for a specific compound that's passed in get request at frontend
    #When running the server, you can test it with this url: http://127.0.0.1:8000/compoundsinfo/?compound_id=1442549
    re_path('compoundsinfo/', views.compoundsResults, name="compoundsResults"),

    # This endpoint would return compound details for a specifc compound that's passed in get request at frontend
    #******Note, not totally functional yet but would return image via bytes here: http://127.0.0.1:8000/compoundimage/?compound_id=1442549
    re_path('compoundimage/', views.get_compound_image, name="get_compound_image")
]
