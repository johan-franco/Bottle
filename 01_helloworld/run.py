#!/usr/bin/env python3
import bottle
import ttg

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
def truthtables(truth = 'P and Q'):
    display = {truth}
    display = print(ttg.Truths(
    ['p', 'q', 'r'],
    ['p => q', 'q => r', '(p => q) or (q => r)'],
    ints=False)
)
    return bottle.template('truthtables', truth_table = display)

bottle.run(host='0.0.0.0', port=8090)
