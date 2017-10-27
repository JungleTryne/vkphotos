import json
from threading import Thread

import bottle
import time
import json

__author__ = 'mishindanila'

import os
import requests
from bottle import post, run, request, route

@route("/")
def hi():
    return "Hi"

@post("/")
def pos():
    print(request.json)
    return "0"

run(host="127.0.0.1", port=os.environ.get('PORT', 5000))
