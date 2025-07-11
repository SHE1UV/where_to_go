from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Place


def fetch_place_details(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related("images"),
        id=place_id
    )

    images_urls = [image.image.url for image in place.images.all()]

    payload = {
        "title": place.title,
        "imgs": images_urls,
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        }
    }

    return JsonResponse(payload, json_dumps_params={"ensure_ascii": False})

