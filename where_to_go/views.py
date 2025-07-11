from django.shortcuts import render
from django.urls import reverse
from places.models import Place


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
