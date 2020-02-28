##############################################################################
#
# Imports

import praw

##############################################################################
#
# Reddit Object - info required to connect to Reddit's API

reddit = praw.Reddit(
	username = "Reddit Account Username",
	password = "Reddit Account Password",
	client_id = "Client Id",
	client_secret = "Client Secret",
	user_agent = "Laptop Search Bot, by /u/SpencerLee_Dev")		
