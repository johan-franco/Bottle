#!/usr/bin/env python3
import bottle

@bottle.route('/')
def index():
     return bottle.template('index')

@bottle.route('/<name>')
def index(name='World'):
    the_message = f'Hello {name}!'
    return bottle.template('template', message=the_message)

@bottle.route('/page1')
def page1():
    return bottle.template('page1')
@bottle.route('/<truth>')
def page1():
    truth = {truth};
    return bottle.template('truthtbales', truth_table = truth)

bottle.run(host='0.0.0.0', port=8090)
