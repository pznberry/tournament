-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database if exists tournament;

create database tournament;

create table Players (Name varchar(30), PlayerID serial primary key);

create table Scores (PlayerID integer references Players(PlayerID), \
	Wins integer, Matches integer);

create table Matches (MatchID serial primary key, Winner integer references \
	Players(PlayerID), Loser integer references Players(PlayerID));






