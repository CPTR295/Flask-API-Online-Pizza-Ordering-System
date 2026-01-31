from flask import current_app,jsonify,request
from app.model.db import AddOns
from app.repository.products import AddOnsRepository
from app.model.config import db_session 

@current_app.post('/addons/add')
def add_addons():
    addons_json = request.get_json()
    addons = AddOns(**addons_json)
    repo = AddOnsRepository(db_session)
    res = repo.insert(addons=addons)
    if res:
        current_app.logger.info('insert addon menu option successful')
        return jsonify(addons_json)
    else:
        current_app.logger.info('insert addon menu encountered a problem')
        return jsonify(message='insert addon menu option encountered a problem')
    
@current_app.get('/addons/list/all')
def list_all_addons():
    repo = AddOnsRepository(db_session)
    recs = repo.select_all()
    addons_rec = [rec.to_json() for rec in recs]
    current_app.logger.info('Retrieved a list of addon menu option successfully')
    return jsonify(addons_rec)