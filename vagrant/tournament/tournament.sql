-- Table definitions for the tournament project.

drop database if exists tournament;

create database tournament;

\c tournament

create table Players (Name varchar(30), PlayerID serial primary key);

create table Scores (PlayerID serial,
	Wins integer, Matches integer);

create table Matches (Winner integer references Players(PlayerID), 
	Loser integer references Players(PlayerID), MatchID serial primary key);






