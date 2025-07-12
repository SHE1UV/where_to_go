from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from .models import Place, Image


PREVIEW_IMAGE_MAX_HEIGHT_PX = 200
PREVIEW_IMAGE_MAX_WIDTH_PX = 300


def preview(obj):
    return format_html(
        "<img src='{}' style='max-height:{}px; max-width:{}px;' />",
        obj.image.url,
        PREVIEW_IMAGE_MAX_HEIGHT_PX,
        PREVIEW_IMAGE_MAX_WIDTH_PX
    )


class ImageInline(SortableTabularInline):
    model = Image
    fields = (
        ("image", preview),
        "ordinal_number"
    )
    readonly_fields = [preview, ]
    extra = 0


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ("title", )
    inlines = [ImageInline, ]
    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = (
        "image",
        preview,
        "place",
        "ordinal_number",
    )
    raw_id_fields = ["place", ]
    readonly_fields = [preview, ]
 
