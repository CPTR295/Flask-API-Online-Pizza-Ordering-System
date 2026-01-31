from flask import current_app,request,jsonify,make_response,Response
from app.model.db import Orders 
from app.repository.orders import OrdersRepository
from app.model.config import db_session
from flask.json import dumps
from json import JSONEncoder
from datetime import date 

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj,date):
                return obj.strftime("%m/%d/%Y, %H:%M:%S")
            iterable = iter(obj) 
        except TypeError:
            pass 
        else:
            return list(iterable)
        return JSONEncoder.default(self,obj)
    
@current_app.post('/order/add')
def add_order():
    order_json =  request.get_json(force=True,silent=True) 
    repo = OrdersRepository(db_session)
    order = Orders(**order_json)
    res = repo.insert(order)
    if res:
        current_app.logger.info('Order post success')
        content = jsonify(order_json)
        return make_response(content,201)
    else:
        content = jsonify(message='Order post error')
        return make_response(content,500)
    
@current_app.get('/order/list/all')
def list_all_order():
    repo = OrdersRepository(db_session)
    recs = repo.select_all()
    o_rec = [rec.to_json() for rec in recs]
    current_app.logger.info('Order get success')
    resp = Response(response=dumps(o_rec,cls=CustomJSONEncoder),status=200,mimetype='application/json')
    return resp 

@current_app.delete('/order/delete/<string:oid>')
def delete_order(oid:str):
   
        repo = OrdersRepository(db_session)
        result = repo.delete(oid)
        if result:
            content = jsonify(message=f'customer {oid} deleted')
            current_app.logger.info('delete order record successful')
            return make_response(content, 201)
        else:
            content = jsonify(message="delete order record encountered a problem")
            return make_response(content, 500)