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

@route('/past')
def past():
    return template('past')

@route('/present')
def present():
    return template('present')

@route('/page2')
def page2():
    return template('page2')
run(host='localhost', reloader=True)