from flask import jsonify, request
from http import HTTPStatus
from app.models.series_model import Series
from psycopg2.errors import UndefinedTable

def series():
    try:
        Series.read_series()
        
    except UndefinedTable:
        Series.create()
        return jsonify({"data": []}), HTTPStatus.OK    
    
    except TypeError:
        return jsonify({"data": []}), HTTPStatus.OK    
    
    serie_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']
    
    series_list = [dict(zip(serie_keys, serie)) for serie in Series.read_series()]
    
    return jsonify({'data': series_list}), HTTPStatus.OK

    
