#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    c.execute("delete from Matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player and score records from the database."""
    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    c.execute("delete from Players;")
    c.execute("delete from Scores;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    c.execute("select count(*) from Players;")
    rows = c.fetchall()
    for row in rows:
        return row[0]
    db.close()


def registerPlayer(name):
    """Registers new player."""
    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    player = "insert into Players values (%s);"
    scores = "insert into Scores (Wins, Matches) values (0, 0);"
    c.execute(player, (name,))
    c.execute(scores)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    """
    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    c.execute("select Scores.PlayerID, Players.Name,\
        Scores.Wins, Scores.Matches\
        from Scores join Players\
        on Scores.PlayerID = Players.PlayerID\
        order by Scores.Wins desc;")
    return c.fetchall()
    db.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    c.execute("insert into Matches (Winner, Loser)\
        values (%s,%s);"%(winner, loser,))
    db.commit()
    db.close()

    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    c.execute("update Scores set Wins = Wins + 1\
        where PlayerID = %s;"%(winner,))
    db.commit()
    db.close()

    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    c.execute("update Scores set Matches = Matches + 1\
        where PlayerID = %s;"%(winner,))
    db.commit()
    db.close()

    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    c.execute("update Scores set Matches = Matches + 1\
        where PlayerID = %s;"%(loser,))
    db.commit()
    db.close()
 
 
def swissPairings():
    """Generates a Swiss Pairing based on number of wins.
    Returns Player ID and Name as tuple.
    """
    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    standings = playerStandings()
    r = []
    for player1, player2 in zip(standings[0::2], standings[1::2]):
        r.append((player1[0], player1[1], player2[0], player2[1]))
    return r
    db.close()

