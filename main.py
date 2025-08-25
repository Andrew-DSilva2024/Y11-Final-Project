from bottle import route, run, template, static_file

@route('/static/<filepath:path>')
def server_statc(filepath):
    return static_file(filepath, root='./static')

@route('/')
def home():
    return template('homepage')

@route('/aboutme')
def aboutme():
    return template('aboutme')

run(host='localhost', reloader=True)