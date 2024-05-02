#!/usr/bin/env python3
import bottle, os


@bottle.get('/')
def index():
    if bottle.request.get_cookie('cookie'):
        mycookie = bottle.request.get_cookie('cookie')
        return bottle.template('cm2', cookie=mycookie)
    else:
        return bottle.template('cm1')


@bottle.post('/')
def index_post():
    mycookie = bottle.request.forms.get('cookie')
    bottle.response.set_cookie('cookie', mycookie)
    return bottle.template('cm2.tpl', cookie=mycookie)


@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    root = os.path.abspath('static')
    return bottle.static_file(filepath, root)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8090)
