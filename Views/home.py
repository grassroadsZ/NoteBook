"""
-*-enconding: utf-8
@Time:2019-09-08 13:43
@Author:grassroadsZ
@File:home.py
Motto：good good study , day day up !!!
"""
from flask import Blueprint, render_template

url_view = Blueprint('url', __name__)

@url_view.route('/')
def index():
    return render_template('hello.html')