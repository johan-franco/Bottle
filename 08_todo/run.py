#!/usr/bin/env python3
import bottle
import sqlite3
import os


@bottle.route('/')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status = '0'")
    result = c.fetchall()
    c.close()
    heading = "The open items are as follows:"
    return bottle.template('make_table', rows=result, heading=heading)


@bottle.route('/new/')
def add_item():
    pass


@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    root = os.path.abspath('static')
    return bottle.static_file(filepath, root)


bottle.debug(True)
bottle.run(reloader=True, host='0.0.0.0', port=8090)
