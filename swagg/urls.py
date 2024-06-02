from django.urls import path, include
from .schemas import schema_view


urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("user/", include("user.urls")),
    path("auth/", include("oauth.urls")),
    path("news/", include("news.urls")),
    path("comment/", include("comments.urls")),
    path("like/", include("likes.urls")),
]