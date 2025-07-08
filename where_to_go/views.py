import json

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from places.models import Place, Image
from django.http import JsonResponse


def show_mainpage(request):
    context = {
        'places': {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [37.62, 55.793676]
                    },
                    "properties": {
                        "title": "«Легенды Москвы",
                        "placeId": "moscow_legends",
                        "detailsUrl": "../static/places/moscow_legends.json"
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [37.64, 55.753676]
                    },
                    "properties": {
                        "title": "Крыши24.рф",
                        "placeId": "roofs24",
                        "detailsUrl": "../static/places/roofs24.json"
                    }
                }
            ]
        }
    }
    return render(request, 'index.html', context)


def fetch_place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images_urls = []
    for image in place.images.all():
        image_url = image.get_absolute_image_url
        images_urls.append(image_url)

    payload = {
        "title": place.title,
        "imgs": images_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    response = JsonResponse(payload, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    return response