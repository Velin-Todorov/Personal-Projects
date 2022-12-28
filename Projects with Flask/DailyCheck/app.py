from flask import Flask, render_template
from . import create_app


app = create_app()

@app.route('/')
def home_page():
    return render_template(
        
        'landing_page.html'
    )
