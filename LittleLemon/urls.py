from django.contrib import admin
from django.urls import include, path

from LittleLemonAPI.views import home


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path(
        "api/",
        include("LittleLemonAPI.urls")
    ),

    path(
        "auth/",
        include("djoser.urls")
    ),

    path(
        "auth/",
        include("djoser.urls.authtoken")
    ),
]