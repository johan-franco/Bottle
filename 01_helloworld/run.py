#!/usr/bin/env python3
import bottle
import ttg

@bottle.route('/')
def index():
     return bottle.template('index')

@bottle.route('/page1')
def page1():
    return bottle.template('page1')

@bottle.route('/truthtables.tpl/<truth>')
def truthtables(truth='P and Q'):
    truth_parts = truth.split()
        
    display = ttg.Truths(['P', 'Q', 'R'],[truth], ints=False)




    
    return bottle.template('truthtables', truth_table=display)
bottle.run(host='0.0.0.0', port=8090)
