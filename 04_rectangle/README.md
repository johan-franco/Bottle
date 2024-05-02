# Rectangle 

This web app again helps demonstrate the get and post protocols. When it
recieves a get request, it renders a web page with a form that asks the user
to enter two dimensions, width and length, and a color choosen from a drop
down menu. The range for width is set between 1 and 200, while length is
set between 1 and 100.

When the user entered values are submitted through a post request, CSS is used
to style a ``<div>`` element with the user entered values used to set the size
of the resulting rectangle on the screen.


## Running Rectangle 

To run this web application, either run:
```
$ python3 run.py
```
or
```
$ python3 run2.py
```
at the command prompt, then point your web browser at ``localhost:8090``.
