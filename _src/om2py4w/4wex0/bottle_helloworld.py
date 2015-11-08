# -*- coding: utf-8 -*-

from bottle import route, run, template

@route('/hello/<name>')
def ind(name):
    return template('<b>Hello {{name}}</b>', name=name)

@route('/test/<name>')
def test(name): 
    return template('<b>Hello {{name}}</b>', name=name)

run(host='localhost', port=8080)
