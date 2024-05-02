# Hello World in a Bottle

This not quite minimal web application is meant to be a good starting point
for learners already familiar with HTML, CSS, and JavaScript.

It maps two URLs, ``/`` and ``/<name>`` to a single function,
``index(name='World')`` which renders a single
[web template](https://en.wikipedia.org/wiki/Web_template_system) named
``template.tpl``, replacing the only templated element, ``{{message}}``,
with either a default value of "Hello World!", or else "Hello {name}!"
where ``{name}`` is a string value passed in through the URL ``/<name>``.

This version of a "Hello World" example is aimed specifically at students in
our web development class who will find ``template.tpl`` to be very familiar.


## Running Hello World in a Bottle

To run this web application, run:
```
$ python3 run.py
```
at the command prompt, then point your web browser at ``localhost:8090``.


## Exercises

1. Change the ``run.py`` file so that it contains the following:
   ```
   #!/usr/bin/env python3
   import bottle

   @bottle.route('/')
   def index():
        return bottle.template('index')

   @bottle.route('/<name>')
   def message(name):
       the_message = f'Hello {name}!'
       return bottle.template('message_template', message=the_message)

   bottle.run(host='0.0.0.0', port=8090)
   ```
   Make required changes to your template (``.tpl``) files so that this
   application works the same way it did before your changes.

2. Instead of a variable in the URL, (``<name>``), URL patterns can contain
   hardcoded strings. Take a look at the following ``run.py``:
   ```
   #!/usr/bin/env python3
   import bottle

   @bottle.route('/')
   def index():
       return bottle.template('index')

   @bottle.route('/page1')
   def page1():
       return bottle.template('page1')

   @bottle.route('/page2')
   def page2():
       return bottle.template('page2')

   bottle.run(host='0.0.0.0', port=8090)
   ```
   Create the required templates to make this work. Add links on each of the
   pages (templates) to link to the others.

3. Create your own application using what you learned in the previous two
   exercises. Create several web pages (using *templates*) and display them
   using different *functions* mapped from different *routes*. In at least
   one of your routes, use a *variable* that gets passed to the function and
   then on to the template.

## Resources

* [Request Routing](https://bottlepy.org/docs/dev/routing.html)
* [SimpleTemplate Engine](https://bottlepy.org/docs/dev/stpl.html)
* [Python | Bottle Web Framework - Part 1](https://www.youtube.com/watch?v=nUcj3d0bI-c) (YouTube video)
