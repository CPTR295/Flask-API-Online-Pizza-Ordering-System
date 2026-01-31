from flask import current_app,request,jsonify,make_response,Response
from app.model.db import Orders 
from app.repository.orders import OrderDetailsRepository
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