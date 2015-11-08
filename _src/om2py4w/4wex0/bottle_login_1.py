# -*-coding: utf-8 -*-

from bottle import get, post, request, run, route, static_file 

@route('/login/:filename') # or @route('/login')
def login(filename):
    return static_file(filename, root='./')

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
def check_login(username, password):
    if (username=="admin") and (password=="admin"):
        return True
    else:
        return False

run(host="localhost", port=8089)
