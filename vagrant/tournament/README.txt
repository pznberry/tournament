Swiss Pairings System
Rebecca Tauber 2015

WHAT IS IT?
-----------

This system utilizes a PostgreSQL database to keep track of
players with unique IDs, matches, and a record of wins and
loses. Using Python functions, the pairing system matches
players of equal strength together (based on number of wins).

REQUIREMENTS
------------

In order to run this pairing system, the latest version of
PostgreSQL must be installed. See www.postgresql.org/download/
for more information. Additionally, Python 2.7.10 can be
downloaded from https://www.python.org/downloads/.
Last, we utilize both VirtualBox VM and Vagrant to access
psql. More information on these can be found at
https://www.virtualbox.org and https://www.vagrantup.com.

CONFIGURATION
-------------

Before running the Python code, the tournament database must
be set up. Log in to vagrant using commands vagrant up and
vagrant ssh. Bring up the front end PostgreSQL terminal by
using the command psql. Database and table definitions can be
found in tournament.sql. Once these tables have been created,
the pairing system is ready to use!

CONTACT
-------

Rebecca Tauber
rctauber@gmail.com