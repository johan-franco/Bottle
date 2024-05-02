#!/usr/bin/env python3
import bottle


@bottle.get('/')
def get():
    f = open('input.html', 'r')
    web_page = f.read()
    f.close()
    return web_page


@bottle.post('/')
def post():
    dimensions = bottle.request.forms
    w = int(dimensions['width'])
    l = int(dimensions['length'])
    dimensions['long'] = str(l) + 'px'
    dimensions['high'] = str(w) + 'px'
    dimensions['area'] = w * l
    dimensions['perimeter'] = 2 * (w + l)

    return bottle.template('output', dimensions)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8090)
