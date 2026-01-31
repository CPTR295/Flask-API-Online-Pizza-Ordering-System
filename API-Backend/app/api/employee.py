from flask import request,jsonify,make_response,current_app
from app.model.db import Employee
from app.model.config import db_session
from app.repository.employee import EmployeeRepository
from app.exceptions.db import DuplicateRecordException,NoRecordException

@current_app.post('/employee/add')
def add_employee():
    emp_json =request.get_json()
    emp = Employee(**emp_json)
    repo = EmployeeRepository(db_session)
    res = repo.insert(emp)
    if res:
        current_app.logger.info('Insert employee success')
        content = jsonify(emp_json)
        return make_response(content,201)
    else:
        raise DuplicateRecordException('Insert Employee Error')
    
@current_app.patch('/employee/update/<string:empid>')
def update_employee_name(empid:str):
    repo = EmployeeRepository(db_session)
    emp_json = request.get_json()
    res = repo.update(empid,emp_json)
    if res:
        content = jsonify(emp_json)
        current_app.logger.info('Employee patch success')
        return make_response(content,201)
    else:
        content = jsonify(message='Error in customer patch')
        raise NoRecordException('Error in employee patch',status_code=500)

@current_app.get('/employee/list/all')
def list_all_employee():
    repo = EmployeeRepository(db_session)
    recs = repo.select_all()
    emps = [rec.to_json() for rec in recs]
    current_app.logger.info('Get all employees')
    return jsonify(emps)

@current_app.put('/employee/update')
def update_employee():
    emp_json = request.get_json()
    repo = EmployeeRepository(db_session)
    res = repo.update(emp_json['empid'],emp_json)
    if res:
        current_app.logger.info('Employee put success')
        content = jsonify(emp_json)
        return make_response(content,201)
    else:
        current_app.logger.info('Employee put error')
        raise NoRecordException('Employee put error',status_code=500)
    
@current_app.delete('/employee/delete/<string:empid>')
def delete_employee(empid:str):
    repo = EmployeeRepository(db_session)
    res = repo.delete(empid)
    if res:
        content = jsonify(message=f'Employee {empid} deleted')
        current_app.logger.info('Employee delete success')
        return make_response(content,201)
    else:
        raise NoRecordException('Employee delete error',status_code=500)