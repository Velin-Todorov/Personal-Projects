# All the views are here
from flask import Flask, render_template, redirect
from app import create_app
from patient_views.views import patients, Views

app = create_app()
# app.register_blueprint(patients)

@app.route('/')
def landing_page():
    """
    This view handles the home page.

    Returns:
        Html for landing page
    """
    return render_template('landing_page.html')