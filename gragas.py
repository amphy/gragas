#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#####################################################################
#
# A smol Python wrapper for using the unofficial League of Legends
# eSports endpoints
#
#####################################################################
class Gragas:

	# This function gets the stats for a particular player ID or name
	def getPlayerStats(self, tournamentId, groupName, searchParam):
		payload = {'tournamentId': tournamentId, 'groupName': groupName}
		r = requests.get('https://api.lolesports.com/api/v2/tournamentPlayerStats', params=payload)
		for playerInfo in r.json()["stats"]:
			if playerInfo["name"].lower() == searchParam.lower() or playerInfo["id"] == searchParam:
				return playerInfo
		return None

	# Functions for getting Player information
	def getPlayerInfo(self, tournamentId, searchParam):
		player = self.getPlayerStats(tournamentId, "regular_season", searchParam)["playerSlug"]
		payload = {'tournament': tournamentId, 'slug': player}

		r = requests.get("https://api.lolesports.com/api/v1/players", params=payload)
		return r.json()["players"][0]

	def getPlayerStatsSummaries(self, tournamentId, searchParam):
		player = self.getPlayerStats(tournamentId, "regular_season", searchParam)["playerSlug"]
		payload = {'tournament': tournamentId, 'slug': player}

		r = requests.get("https://api.lolesports.com/api/v1/players", params=payload)
		return r.json()["playerStatsSummaries"][0]

	def getPlayerStatsHistories(self, tournamentId, searchParam):
		player = self.getPlayerStats(tournamentId, "regular_season", searchParam)["playerSlug"]
		payload = {'tournament': tournamentId, 'slug': player}

		r = requests.get("https://api.lolesports.com/api/v1/players", params=payload)
		return r.json()["playerStatsHistories"][0]

	# Functions for getting League information
	def getAllLeagueInfo(self, leagueId):
		s = "https://api.lolesports.com/api/v1/leagues/" + str(leagueId)
		r = requests.get(s)

		return r.json()

	def getLeagueInfo(self, leagueId):
		s = "https://api.lolesports.com/api/v1/leagues/" + str(leagueId)
		r = requests.get(s)

		return r.json()["leagues"][0]

	def getLeagueTournamentInfo(self, leagueId):
		s = "https://api.lolesports.com/api/v1/leagues/" + str(leagueId)
		r = requests.get(s)

		return r.json()["highlanderTournaments"]

	def getLeagueTournamentRecords(self, leagueId):
		s = "https://api.lolesports.com/api/v1/leagues/" + str(leagueId)
		r = requests.get(s)

		return r.json()["highlanderRecords"]

	def getLeagueTeams(self, leagueId):
		s = "https://api.lolesports.com/api/v1/leagues/" + str(leagueId)
		r = requests.get(s)

		return r.json()["teams"]

	# Functions for getting match details
	def getAllMatchDetails(self, tournamentId, matchId):
		payload = {'tournamentId': tournamentId, 'matchId': matchId}
		r = requests.get('https://api.lolesports.com/api/v2/highlanderMatchDetails', params=payload)

		return r.json()

	def getMatchTeams(self, tournamentId, matchId):
		payload = {'tournamentId': tournamentId, 'matchId': matchId}
		r = requests.get('https://api.lolesports.com/api/v2/highlanderMatchDetails', params=payload)

		return r.json()["teams"]

	def getMatchPlayers(self, tournamentId, matchId):
		payload = {'tournamentId': tournamentId, 'matchId': matchId}
		r = requests.get('https://api.lolesports.com/api/v2/highlanderMatchDetails', params=payload)

		return r.json()["players"]

	def getMatchScheduleItems(self, tournamentId, matchId):
		payload = {'tournamentId': tournamentId, 'matchId': matchId}
		r = requests.get('https://api.lolesports.com/api/v2/highlanderMatchDetails', params=payload)

		return r.json()["scheduleItems"]

	def getMatchGameIdMappings(self, tournamentId, matchId):
		payload = {'tournamentId': tournamentId, 'matchId': matchId}
		r = requests.get('https://api.lolesports.com/api/v2/highlanderMatchDetails', params=payload)

		return r.json()["gameIdMappings"]

	def getMatchVideos(self, tournamentId, matchId):
		payload = {'tournamentId': tournamentId, 'matchId': matchId}
		r = requests.get('https://api.lolesports.com/api/v2/highlanderMatchDetails', params=payload)

		return r.json()["videos"]

	# Get Team Info for a team by id or name
	def getAllTeamInfo(self, leagueId, tournamentId, searchParam):
		slug = self.getTeamSlug(leagueId, searchParam)
		payload = {'slug': slug, 'tournament': tournamentId}

		r = requests.get("https://api.lolesports.com/api/v1/teams", params=payload)
		return r.json()

	def getTeamPlayers(self, leagueId, tournamentId, searchParam):
		slug = self.getTeamSlug(leagueId, searchParam)
		payload = {'slug': slug, 'tournament': tournamentId}

		r = requests.get("https://api.lolesports.com/api/v1/teams", params=payload)
		return r.json()["players"]

	def getTeamRosterStats(self, leagueId, tournamentId, searchParam):
		slug = self.getTeamSlug(leagueId, searchParam)
		payload = {'slug': slug, 'tournament': tournamentId}

		r = requests.get("https://api.lolesports.com/api/v1/teams", params=payload)
		return r.json()["teamRosterStats"]

	# Function to get schedule items for League of Legends games
	def getScheduleItems(self, leagueId):
		r = requests.get("https://api.lolesports.com/api/v1/scheduleItems", params={'leagueId': leagueId})

		return r.json()

	# Helper functions for common functions
	def getTeamSlug(self, leagueId, searchParam):
		teams = self.getLeagueTeams(leagueId)
		for team in teams:
			if searchParam.lower() == team["name"].lower() or searchParam == team["id"] or searchParam.lower() == team["acronym"].lower():
				return team["slug"]
		return None

	def getTournamentId(self, leagueId, searchParam):
		tournaments = self.getLeagueTournamentInfo(leagueId)
		for tournament in tournaments:
			if tournament["title"].lower() == searchParam.lower():
				return tournament["id"]
		return None

