from flask import current_app   ,jsonify,request,Response,abort
from app.model.db import Login
from app.model.config import db_session
from app.repository.login import LoginRepository
from flask.json import dumps,loads

@current_app.route('/login/add',methods=['GET'])
def add_login():
    if request.is_json:
        login_json = loads(request.data)
        login = Login(**login_json)
        repo = LoginRepository(db_session)
        res = repo.insert(login)
        if res:
            current_app.logger.info('Login post success')
            return jsonify(login_json)
        else:
            abort(500,description='Insert post error')
    else:
        abort(500)

@current_app.patch('/login/password/update/<string:username>')
def update_password(username:str):
    login_json = request.get_json()
    repo  = LoginRepository(db_session)
    res = repo.update(username,login_json)
    if res:
        current_app.logger.info('update patch success')
        return jsonify(login_json)
    else:
        abort(500,description='Update patch error')

@current_app.route('/login/list/all',methods=['GET'])
def list_all_login():
    repo = LoginRepository(db_session)
    recs = repo.select_all()
    log_rec = [rec.to_json() for rec in recs]
    current_app.logger.info('Login get  success')
    resp = Response(response=dumps(log_rec),status=200,mimetype='application/json')
    return resp