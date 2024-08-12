from flask import render_template, redirect, url_for, flash, request
from plantapp import app, db
from plantapp.models import Category, Recipe


@app.route("/")
def home():
    return render_template("base.html")
