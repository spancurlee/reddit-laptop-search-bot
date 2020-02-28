##############################################################################
#
# Imports

import praw
from config import reddit
from collections import defaultdict

##############################################################################
#
# Constants

MESSAGE_TOO_LONG = "TOO_LONG"

##############################################################################
#
# Public Function

def send_message(user_specs:list, links:defaultdict):
	"""
	Sends user a message containing the links of the laptops that match the specified criteria
	"""
	print("Sending list to reddit inbox...")
	try:
		message_title =  _create_message_title(user_specs)
		message = _create_message(links)
		reddit.redditor(reddit.config.username).message(message_title, message)
		print("List sent successfully!")
	except Exception as e:
		if e.error_type == MESSAGE_TOO_LONG:
			print("List exceeds max text length")
			_send_short_list(message_title,message)
		else:
			print(e)

##############################################################################
#
# Private Function

def _create_message_title(user_specs:list)->list:
	"""
	Turns list items in user_specs into string and returns it as the title
	"""
	message_title = " ".join([spec if type(spec) == str else ", ".join(spec) for spec in user_specs]) + " Laptops"
	return message_title

def _create_message(links:defaultdict):
	"""
	Creates the message
	link[0] = submission link, link[1] = direct link
	"""
	message = ""
	count = 1
	for title,links in links.items():
		laptop_info = "{}) {}\n\nSubmiission Link:\n {}\n\nLaptop Link:\n\n {}\n\n".format(count,title,links[0],links[1])
		message+=laptop_info
		count+=1
	return message

def _send_short_list(message_title:str, text:str):
	"""
	Sends the top 5 submissions
	"""
	try:
		print("Sending top 5 submissions...")
		cutoff = text.find("6)")
		shortened_list = text[0:cutoff]
		reddit.redditor(reddit.config.username).message(message_title, shortened_list)
		print("List sent successfully!")
	except Exception as e:
		print(e)
