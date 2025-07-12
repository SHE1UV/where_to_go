from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from places.views import show_main_page, fetch_place_details


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", show_main_page, name="main_page"),
    path("places/<int:place_id>/", fetch_place_details, name="place_details"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
