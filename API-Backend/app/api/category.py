from flask import jsonify,request,current_app,abort
from app.model.db import Category
from app.repository.products import CategoryRepository
from app.model.config import db_session 
from app.exceptions.db import NoRecordException

@current_app.post('/category/add')
def add_category():
    if request.is_json():
        cat_json = request.json
        cat = Category(**cat_json)
        repo = CategoryRepository(db_session)
        res = repo.insert(cat)
        if res:
            current_app.logger.info('insert category details success')
            return jsonify(cat_json)
        else:
            current_app.logger.info('error in category insert')
            return jsonify(message='error in category insert')
    else:
        current_app.logger.info('Invalid request')
        abort(500)

@current_app.get('/category/list/all')
def list_all_category():
    repo = CategoryRepository(db_session)
    recs = repo.select_all()
    cat_rec = [rec.to_json() for rec in recs]
    current_app.logger.info('Retrived a list of categories')
    return jsonify(cat_rec)

@current_app.delete('/category/delete/<int:id>')
def delete_category(id:int):
    repo = CategoryRepository(db_session)
    res = repo.delete(id=id)
    if res:
        current_app.logger.info('Delete Category success')
        return jsonify(message=f'Category {id} deleted'),201
    else:
        raise NoRecordException("Error in delete category record",status_code=500)