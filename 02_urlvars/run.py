#!/usr/bin/env python3
import bottle


@bottle.route('/')
def welcome():
    return bottle.template('welcome')
@bottle.route('/<name>')
def name(name = ''):
    the_message = f'The name {name} was passed to me!'
    print(the_message)
    return bottle.template('message', message = the_message)
@bottle.route('/<name>/<number>')
def different_index(name='', number=''):
    the_message = f'Received name {name} and number {number}!'
    print(the_message)
    return bottle.template('message', message=the_message)
@bottle.route('/<name>/<number>/<lastname>')
def last_name(name='', number= '',lastname=''):
    the_message = f'Received name {name}, last name {lastname}, and number {number}!'
    print(the_message)
    return bottle.template('message', message=the_message)


bottle.run(host='0.0.0.0', port=8090)
