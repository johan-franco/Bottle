#!/usr/bin/env python3
import bottle
import sqlite3


def get_next_location(hero, direction, cur):
    s = """SELECT newlocation FROM Path WHERE
              location = {0} and direction = '{1}'"""
    cur.execute(s.format(hero, direction))
    results = cur.fetchall()
    if not results:
        return hero
    return results[0][0]


def get_location(hero, cur):
    s = "SELECT name, description FROM Location WHERE id = {0}"
    cur.execute(s.format(hero))
    results = cur.fetchall()
    return results[0][0], results[0][1]


@bottle.get('/')
def welcome():
    db = sqlite3.connect('places_n_paths.db')
    cur = db.cursor()
    our_hero = 0
    loc = get_location(our_hero, cur)

    return bottle.template('templates/welcome.tpl', loc=loc[0], desc=loc[1])


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8090)
