from flask import Blueprint
from app.controllers import create_controller, select_by_id_controller, series_controller

bp = Blueprint('series', __name__)

bp.get("")(series_controller.series)

bp.post("")(create_controller.create)

bp.get("/<int:serie_id>")(select_by_id_controller.select_by_id)

