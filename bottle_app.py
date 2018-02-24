
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template
from bottle import get, post, request

@get('/')
def getInput():
    return template("input.html")

@post('/output')
def out():
    txtInput = request.forms.get('txtInput')
    return template("output.html", txtInput = txtInput)

@route('/secret')
def secret():
    return 'How did you get here? This is classified! Out with you!'

application = default_app()
