from django.urls import path

from .views import home, AboutView

app_name = 'pages'

urlpatterns = [
    path("", home, name="home"),
    path("about/", AboutView.as_view(), name="about"),
]