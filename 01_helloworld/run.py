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

@bottle.route('/truthtables/<truth>')
def truthtables(truth='P and Q'):
    truth_parts = truth.split()
    
    variables = set(part for part in truth_parts if part.isalpha())
    
    display = ttg.Truths(variables, [truth], ints=False)
    
    return bottle.template('truthtables', truth_table=display)
bottle.run(host='0.0.0.0', port=8090)
