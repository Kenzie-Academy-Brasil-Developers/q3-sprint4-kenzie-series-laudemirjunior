from flask import jsonify
from http import HTTPStatus
from app.models.series_model import Series

def select_by_id(serie_id):
    serie_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']
    
    series_list = [dict(zip(serie_keys, serie)) for serie in Series.read_series_by_id(serie_id)]
    
    if series_list == []:
        return jsonify({"error": "Not Found"}), HTTPStatus.NOT_FOUND

    return jsonify({'data': series_list[0]}), HTTPStatus.OK