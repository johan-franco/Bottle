# A Name And a Number 

This web app builds on [Hello World!](01_helloworld), by extending the concept
of URL mapping to handle three different URLs, ``/``, ``/<name>``, and
``/<name>/<number>``, all mapped again to a single function, this time named
``different_index(...)``, so that it is clear the function name is arbitrary.

This time two different templates are used, ``welcome.tpl`` , which is
rendered when ``/`` is the URL, and ``message.tpl``, which renders for
``/<name>`` and ``/<name>/<number>``. Both templates *rebase* a parent
template, ``layout.tpl``.

To understand how Bottle's templates work, read the
[SimpleTemplate Engine](https://bottlepy.org/docs/stable/stpl.html) docs.


## Running An Name And a Number

To run this web application, run:
```
$ python3 run.py
```
at the command prompt, then point your web browser at ``localhost:8090``.


## Resources

* [SimpleTemplate Engine](https://bottlepy.org/docs/stable/stpl.html)
