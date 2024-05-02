# A Tiny ToDo List App Using Bottle

The main goal of this app is to explore connecting to an
[SQLite](https://en.wikipedia.org/wiki/SQLite) database from
[Bottle](https://bottlepy.org/docs/stable/).

When originally started the plan was to use Python's
[sqlite3](https://docs.python.org/3/library/sqlite3.html) library directory,
but with my recent discover of the
[Bottle-SQLite](https://bottlepy.org/docs/stable/plugins/sqlite.html), I plan
to use that instead.


## Setup

The database file ``todo.db`` needs to be present for this app to work. It
can be created and populated with some test data by running:
```
$ sqlite3 todo.db < resources/make_todo_db.sql
```
