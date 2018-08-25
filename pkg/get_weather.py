import requests as r
import json
from datetime import datetime
from sys import exit

from .config import BASE_URI, SECRET_KEY, LAT, LONG, HRS


def get_raw_data(endpoint, latitude, longitude):
    lat_long = latitude + ',' + longitude
    elements = [BASE_URI, endpoint, SECRET_KEY, lat_long]
    req_url = '/'.join(elements)
    resp = r.get(req_url)
    check_response(resp)
    resp_json = resp.json()
    return resp_json


def check_response(response):
    if response.status_code == 200:
        pass
    else:
        print('Bad Response: Response Code %d' % response.status_code)


def get_todays_weather():
    response = get_raw_data('forecast', LAT, LONG)
    today_hourly = response["hourly"]
    now = response['currently']['time']
    hours = [t['time'] for t in today_hourly["data"]
             if t['time'] - now <= HRS * 3600]
    return today_hourly


def get_temp_range(data):
    temps = [ a['apparentTemperature'] for a in data['data']]
    min_temp = min(temps)
    max_temp = max(temps)
    return min_temp, max_temp


def get_max_precip(data):
    prec = [ a['precipProbability'] for a in data['data']]
    max_prec = max(prec)
    return max_prec


def get_max_avg_hum(data):
    hum = [ a['humidity'] for a in data['data']]
    max_hum = max(hum)
    return max_hum
