from flask import Blueprint

home_bp = Blueprint('home_bp',template_folder='pages',
                    static_folder='resources',static_url_path='static')

import app.home.views.home