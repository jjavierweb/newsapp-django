# import django url path
from django.urls import path

# import views
from .views import HomePageView

# add urlpatterns
urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
]
