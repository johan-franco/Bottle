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
    words = {}
    words['name'] = bottle.request.forms.get('name')
    words['place'] = bottle.request.forms.get('place')
    words['relation'] = bottle.request.forms.get('relation')
    words['thing'] = bottle.request.forms.get('thing')
    words['action'] = bottle.request.forms.get('action')
    words['organ'] = bottle.request.forms.get('organ')
    words['adj1'] = bottle.request.forms.get('adj1')
    words['adj2'] = bottle.request.forms.get('adj2')
    words['adj3'] = bottle.request.forms.get('adj3')
    words['thing2'] = bottle.request.forms.get('thing2')

    return bottle.template('story', words)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8090)
