from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


def show_main_page(request):
    places = Place.objects.all()

    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place_details', kwargs={"place_id": place.id})
            }
        } for place in places
    ]

    context = {
        "places": {
            "type": "FeatureCollection",
            "features": features
        }
    }

    return render(request, "index.html", context)


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
