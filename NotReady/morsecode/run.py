#!/usr/bin/env python3
import bottle
from morsecode import eng2morse, morse2eng


@bottle.get('/')
def index():
    return bottle.template('views/welcome')


@bottle.route('/tomorse', method='GET')
def tomorse():
    morse = ''

    if bottle.request.GET.get('save', '').strip():
        ne_string = bottle.request.GET.get('Translater', '').strip()
        s = ne_string.upper()
        morse = eng2morse(s)

    return bottle.template('views/gettrans', display=morse,
                           targetpage='/toenglish', source='English',
                           helptext='', target='morse', sourcepage='/tomorse')


@bottle.route('/toenglish', method='GET')
def toenglish():
    english = ''

    if bottle.request.GET.get('save', '').strip():
        ne_string = bottle.request.GET.get('Translater', '').strip()
        s = ne_string.upper()
        english = morse2eng(s)

    ht1 = 'Make sure it is formatted with spaces between each letter and a '
    ht2 = 'slash between each word.'
    helptext = ht1 + ht2

    return bottle.template('views/gettrans', display=english,
                           targetpage='/tomorse', source='morse',
                           helptext=helptext, target='English',
                           sourcepage='/toenglish')


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8090)
