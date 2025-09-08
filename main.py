from bottle import route, run, template, static_file

@route('/static/<filepath:path>')
def server_statc(filepath):
    return static_file(filepath, root='./static')

@route('/')
def home():
    return template('homepage2')

@route('/sacred')
def sacred():
    return template('sacredheartcopy')

@route('/aboutme')
def aboutme():
    return template('aboutme')
run(host='localhost', reloader=True)