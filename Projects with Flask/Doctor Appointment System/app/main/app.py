# All the views are here
from flask import Flask, render_template, redirect
from app import create_app


app = create_app()

@app.route('/')
def landing_page():
    """
    This view handles the home page.

    Returns:
        Html for landing page
    """
    return render_template('landing_page.html')