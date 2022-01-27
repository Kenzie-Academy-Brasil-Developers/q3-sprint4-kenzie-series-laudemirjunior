from flask import jsonify, request
from http import HTTPStatus
from app.models.series_model import Series
from psycopg2.errors import UniqueViolation

def create():
    
    Series.create()
    
    data = request.get_json()
    
    serie = Series(**data)
    
    try:
        inserted_serie = serie.create_serie()
    
    except UniqueViolation as error:
        return (
            jsonify({"msg": error.args}), HTTPStatus.UNPROCESSABLE_ENTITY
        )
        
    serie_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']
    
    inserted_serie = dict(zip(serie_keys, inserted_serie))
    
    return jsonify(inserted_serie), HTTPStatus.CREATED