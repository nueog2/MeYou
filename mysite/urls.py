from django.contrib import admin
from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index),
    path("<int:content_id>/", views.detail, name="detail"),
    path(
        "comment/create/<int:content_id>/", views.comment_create, name="comment_create"
    ),
    path(
        "comment/update/<int:comment_id>/", views.comment_update, name="comment_update"
    ),
    path(
        "comment/delete/<int:comment_id>/", views.comment_delete, name="comment_delete"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
