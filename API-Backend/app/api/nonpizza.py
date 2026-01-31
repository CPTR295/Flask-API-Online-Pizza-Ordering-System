from flask import current_app,jsonify,request,abort
from app.model.db import NonPizza
from app.repository.products import NonPizzaRepository
from app.model.config import db_session

@current_app.post('/nonprizza/add')
def add_nonpizza():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        nonpizza_json = request.json
        nonprizza = NonPizza(**nonpizza_json)
        repo = NonPizzaRepository(db_session)
        res = repo.insert(nonprizza)
        if res:
            current_app.logger.info('Nonpizza post success')
            return jsonify(nonpizza_json)
        else:
            current_app.logger.info('Non_pizza post error')
            return jsonify(message='Non_pizza post error')
    else:
        abort(500)

@current_app.get('/nonpizza/list/all')
def list_all_nonpizza():
    repo = NonPizzaRepository(db_session)
    recs = repo.select_all()
    np_recs = [rec.to_json() for rec in recs]
    current_app.logger.info('Nonpizza get success')
    return jsonify(np_recs)