from flask import Blueprint, typing as ft, render_template
from flask.views import View


patients = Blueprint(
    'patients', 
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/patients"
)

class HomeView(View):
    def dispatch_request(self):
        return render_template('')

class LoginView(View):
    def dispatch_request(self):
        return render_template('login_page.html')
    
# login_view_func = Views.as_view('login', template='login_page.html')
# register_view_func = Views.as_view('register', template='register_page.html')

patients.add_url_rule(
    '/login/', 
    view_func=LoginView.as_view('login')
)

# patients.add_url_rule(
#     '/register/',
#     view_fund=register_view_func
# )