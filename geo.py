import requests
from math import sin, cos, sqrt, atan2, radians


def get_geo_info(city_name, type_info):
    url = "https://geocode-maps.yandex.ru/1.x/"

    params = {
        'geocode': city_name,
        'format': 'json',
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b"
    }

    response = requests.get(url, params)
    json = response.json()
    if type_info == "country":
        return json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'] \
            ['GeocoderMetaData']['AddressDetails']['Country']['CountryName']
    elif type_info == "coordinates":
        point_str = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        point_array = [float(x) for x in point_str.split(' ')]
        return point_array
    else:
        return {'error': f'type_info не может быть { type_info } Используйте country или coordinates'}


def get_distance(p1, p2):

    R = 6373.0

    lon1 = radians(p1[0])
    lat1 = radians(p1[1])
    lon2 = radians(p2[0])
    lat2 = radians(p2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance