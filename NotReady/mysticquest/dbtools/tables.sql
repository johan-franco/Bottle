CREATE TABLE Location (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT
);
CREATE TABLE Path (
    location INTEGER,
    direction TEXT,
    newlocation INTEGER
);
