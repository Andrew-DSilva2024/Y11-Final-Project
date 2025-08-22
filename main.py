from bottle import route, run, template, static_file

@route('/static/<filepath:path>')
def server_statc(filepath):
    return static_file(filepath, root='./static')

@route('/')
def home():
    return template('homepage')

@route('/past')
def past():
    return template('past')

run(host='localhost', reloader=True)