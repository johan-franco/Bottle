#!/usr/bin/env python3
import bottle
import random


@bottle.route("/")
@bottle.route("/<string>")
def gen(string=""):
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in range(8):
        string += a[random.randrange(0, 25)]
    return bottle.template("present", string=string)


# Use this instead of bottle.run() if you are using Google App Engine.
# bottle.run(server="gae")
bottle.run()
