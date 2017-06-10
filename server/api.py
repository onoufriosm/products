# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify, request

api = Blueprint('api', __name__)


def data_path(filename):
    data_path = current_app.config['DATA_PATH']
    return u"%s/%s" % (data_path, filename)


@api.route('/search', methods=['GET'])
def search():
    params = getSearchParameters(request.args)

    if not validateSearchParameters(params):
        return jsonify({'error': 'Parameters not valid'}), 400

    products = getProducts(params)

    return jsonify({'products': products})

def getSearchParameters(data):
    count = int(data.get('count'))
    radius = int(data.get('radius'))
    lat = float(data.get('lat'))
    lng = float(data.get('lng'))
    tags = data.get('tags')

    return {'count': count, 'radius': radius, 'lat': lat, 'lng': lng, 'tags': tags}

def validateSearchParameters(params):
    validCount = (params['count'] and params['count'] in [10, 20, 50])
    validRadius = (params['radius'] and params['radius'] in [100, 500, 1000, 2000])
    validLat = (params['lat'] < 90 and params['lat'] > -90)
    validLng = (params['lng'] < 180 and params['lng'] > -180)

    print(validCount)

    return validCount and validRadius and validLat and validLng;

def getProducts(params):
    # if tags included, get only shops that have particular tag
    # + within radius 
    # N most popular
    return []
























