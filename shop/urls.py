from django.urls import path

from shop.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]