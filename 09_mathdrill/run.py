#!/usr/bin/env python3
#
# Copyright (C) Alex Hirschberg and Jeffrey Elkner
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
import bottle
import os
import random

curdir = os.path.dirname(os.path.abspath(__file__))
bottle.TEMPLATE_PATH.insert(0, curdir + '/views/')

students = [line.strip() for line in open('students.txt')]
questions = [eval(line.strip()) for line in open('questions.txt')]


@bottle.route('/')
def index():
    student = students[random.randint(0, len(students) - 1)]
    question = questions[random.randint(0, len(questions) - 1)]

    return bottle.template('drill.tpl',
                           imgpath="/static/img/" + question[1],
                           imgalt="Question",
                           csspath="/static/css/drill.css",   
                           student=student,
                           question=question[0])


@bottle.route('/static/:path#.+#')
def server_static(path):
    return bottle.static_file(path, root=curdir + "/static/")


bottle.run(host='0.0.0.0', port=8090)
