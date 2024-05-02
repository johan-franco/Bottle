#!/usr/bin/env python3
import bottle


@bottle.get('/')
def get():
    f = open('parts.html', 'r')
    web_page = f.read()
    f.close()
    return web_page 


@bottle.post('/')
def post():
    words = bottle.request.forms
    return bottle.template('story', words)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8090)
