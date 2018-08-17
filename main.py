from pkg.get_weather import get_temp_range,get_todays_weather,get_max_precip

from utils.db_functions import connect_to_db

WEATHER = get_todays_weather()

def get_clothes_rec():
    low, high = get_temp_range(WEATHER)
    temp_int = int(low)
    db = connect_to_db()
    curs = db.cursor()
    curs.execute("SELECT clothes from temperature where temperature = %d" % temp_int)
    rec = curs.fetchone()[0]
    return rec, low, high


def get_rain_rec():
    prec = get_max_precip(WEATHER)
    if prec >= .25:
        rec = 'Bring your umbrella!'
    else:
        rec = ''
    return rec
