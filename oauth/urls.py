from django.urls import path

from oauth.views import TokenView

urlpatterns = [
    path("auth/", TokenView.as_view(), name="auth"),
]