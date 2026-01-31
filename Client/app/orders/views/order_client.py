import requests 
from app.orders import orders_client_bp
from flask import render_template,request

@orders_client_bp.route('/client/order/add',methods=['GET','POST'])
def add_order():
    if request.method == 'POST':
        order_dict = request.form.to_dict(flat=True) 
        order_add_api = "http://localhost:5000/order/add"
        resp:requests.Response = requests.post(order_add_api,json=order_dict)
    
    customer_list_api = "http:localhost:5000/customer/list/all"
    employee_list_api = "http:localhost:5000/employee/list/all"

    resp_customer:requests.Response = requests.get(customer_list_api)
    resp_employee:requests.Response = requests.get(employee_list_api)

    return render_template('add_order.html',customers=resp_customer.json(),employees = resp_employee.json())