from flask import render_template, request
from . import app

@app.route("/")
def index():
    return "Welcome to Payroll Management System"
