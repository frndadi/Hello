# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 00:00:00 2024

@author: Rentorzo
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def helloworld():
    return "Weather is cold today"


if __name__ == "__main__":
    app.run()
