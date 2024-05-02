#!/usr/bin/env python3
import bottle, random


@bottle.get('/')
def index():
    number = random.randint(1, 1000)
    guesscount = 0

    gamestate = "{0}:{1}".format(number, guesscount)
    bottle.response.set_cookie('gamestate', gamestate)

    return bottle.template('start.tpl')


@bottle.post('/')
def index_post():
    gamestate = bottle.request.get_cookie('gamestate')
    number, guesscount = gamestate.split(':')
    number = int(number)
    guesscount = int(guesscount) + 1
    guess = int(bottle.request.forms.get('guess'))

    if guess > number:
        message = "Too high"
    elif guess < number:
        message = "Too low"
    else:
        return bottle.template('win', guesscount=guesscount)

    gamestate = "{0}:{1}".format(number, guesscount)
    bottle.response.set_cookie('gamestate', gamestate)

    return bottle.template('again', message=message, guesscount=guesscount)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8090)
