from flask import Blueprint, typing as ft, render_template
from flask.views import View, MethodView


patients = Blueprint(
    'patients', 
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/patients"
)

class Views(View):
    def __init__(self, template):
        self.template = template


    def dispatch_request(self):
        return render_template(self.template)
    
login_view_func = Views.as_view('login', template='login_page.html')
register_view_func = Views.as_view('register', template='register_page.html')

patients.add_url_rule(
    '/login/', 
    view_func=login_view_func
)

patients.add_url_rule(
    '/register/',
    view_fund=register_view_func
)