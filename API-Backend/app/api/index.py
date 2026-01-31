from flask import current_app,request,jsonify,make_response,Response
from flask.json import dumps 
from datetime import date

@current_app.get('/index2')
def index2():
    books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': date.today()},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': date.today()},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': date.today()}
    ]
    resp = Response(response=dumps(books),status=200,mimetype='application/json')
    return resp 

@current_app.post('/accept')
def accept_json():
    print(request.get_json())
    return 'success',201 

@current_app.patch('/accept')
def accespt_patch():
    print(request.get_json())
    return 'Success',201

@current_app.route("/index", methods = ['GET'])
def index():
   response = make_response(jsonify(message='This is an Online Pizza Ordering System.', today=date.today()), 200)
   return response

@current_app.route("/introduction", methods = ['GET'])
def introduction():
   response = make_response(jsonify('This is an application that accepts orders based on the offered menus, generates order requests, and provides payment receipts.'), 200)
   return response


@current_app.route("/company/trademarks", methods = ['GET'])
def list_goals():
   response = make_response(jsonify(['Eat', 'Live', 'Happy']), 200)
   return response