CREATE TABLE todo (
  id INTEGER PRIMARY KEY,
  task char(100) NOT NULL,
  status bool NOT NULL
);
INSERT INTO todo (task,status) VALUES (
  'Read Beginning Python Programming for Aspiring Web Developers to get a good introduction into Python',
  0
);
INSERT INTO todo (task,status) VALUES (
  'Visit the Python website for more info on Python',
  0
);
INSERT INTO todo (task,status) VALUES (
  'Pass your PCEP certification',
  0
);

INSERT INTO todo (task,status) VALUES (
  'Configure your Python programming environment',
  0
);
INSERT INTO todo (task,status) VALUES (
  'Choose your favorite WSGI-Framework',
  0
);
INSERT INTO todo (task,status) VALUES (
  'Create your first web app',
  0
);
