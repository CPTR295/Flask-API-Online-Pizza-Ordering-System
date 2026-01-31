from flask import current_app,jsonify,request,make_response
from app.model.config import db_session
from app.model.db import Customer
from app.repository.customer import CustomerRepository

@current_app.post('/customer/add')
def add_customer():
    cust_json = request.get_json()
    repo = CustomerRepository(db_session)
    cus = Customer(**cust_json)
    res = repo.insert(cus)
    if res : 
        current_app.logger.info('Insert customer success')
        content = jsonify(cust_json)
        return make_response(content,201)
    else:
        content = jsonify(messgae='insert customer error')
        return make_response(content,500)
    
@current_app.get('/customer/list.all')
def list_all_customer():
    repo = CustomerRepository(db_session)
    recs = repo.select_all()
    cust_recs = [rec.to_json() for rec in recs]
    current_app.logger.info('retrieved list of customer')
    return make_response(jsonify(cust_recs),201)

@current_app.patch('/customer/update/<string:cid>')
def update_customer(cid:str):
    cus_json = request.get_json()
    repo = CustomerRepository(db_session)
    res = repo.update(cid,cus_json)
    if res:
        content = jsonify(cus_json)
        current_app.logger.info('Update/patch Customer Success')
        return make_response(content,201)
    else:
        content = jsonify(message='Error in customer patch')
        current_app.logger.info('Error in customer patch')
        return make_response(content,500)

@current_app.put('/customer/update')
def update_customer():
    cus_json = request.get_json()
    repo = CustomerRepository(db_session)
    res = repo.update(cus_json['id'],cus_json)
    if res:
        content = jsonify(cus_json)
        current_app.logger.info('Update/put Customer Success')
        return make_response(content,201)
    else:
        content = jsonify(message='Error in customer update')
        current_app.logger.info('Error in customer update')
        return make_response(content,500)
    
@current_app.delete('/customer/delete/<string:cid')
def delete_customer(cid:str):
    repo = CustomerRepository(db_session)
    res = repo.delete(cid)
    if res:
        content = jsonify(message=f'Customer {cid} delete')
        current_app.logger.info('Customer deleted')
        return make_response(content,201)
    else:
        content = jsonify(message='delete customer error')
        return make_response(content,500)