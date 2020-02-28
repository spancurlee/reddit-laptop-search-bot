##############################################################################
#
# Imports

import time
from collections import defaultdict
from config import reddit
import sys

##############################################################################
#
# Constants

SUBREDDIT = "LaptopDeals"
REDDIT_FORMAT = "https://www.reddit.com"
NONE_BMP_CHAR = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd) # Maps all codepoints outside the BMP, from 0xFFFF to to U+FFFD 
																		  # Used to translate the submission titles that contains characters outside of the Basic Multilingual Plane

##############################################################################
#
# Public Function

def search_submissions(user_specs:list, notification_on = False):
 	"""
 	Searches through /r/LaptopDeals for submissions that match the given specs

 	The keys in the defaultdict, links, will be the submission title while the
 	values will be a list containing the permalink as the first item and the
 	direct url to purchase the laptop as the second item
	
	new_link will represent whehter the submission is new when notifactions are
	turned on, otherwise new_link will be set to True 

 	"""
 	print("\nFinding submissions...")
 	while True:
 		try:
 			links = defaultdict(list) 
 			submission_stream = reddit.subreddit(SUBREDDIT).hot(limit = 150) if notification_on == False else reddit.subreddit(SUBREDDIT).new(limit = 150)
 			start_time = time.time()
 			for submission in submission_stream:
 				submission_title = submission.title.translate(NONE_BMP_CHAR) 
 				good_link = _match_specs(user_specs,submission,submission_title)
 				new_link = submission.created_utc > start_time if notification_on == True else True
 				if good_link == True and new_link == True:
 					submission_link = REDDIT_FORMAT + submission.permalink
 					links[submission_title] = [submission_link,submission.url]
 			return links
 		except Exception as e:
 			print(e)

##############################################################################
#
# Private Functions

def _match_specs(user_specs:list, submission, submission_title:str)->bool:
	"""
	Checks whether the specs are found in the submission
	
	Returns False if submissions does not contain links to purchase laptop
	or if the submission is pinned

	Will return true is user_specs' length is 0

	"""
	if REDDIT_FORMAT in submission.url or submission_title[0] == "\\":  
		return False
		
	if len(user_specs) == 0:
		return True
	else:
		for specs in user_specs:
			if type(specs) == str and specs.lower() not in submission_title.lower():
				return False
			elif type(specs) == list:
				at_least_one = False
				for spec in specs:
					if spec.lower() in submission_title.lower():
						at_least_one = True
				if at_least_one == False:
					return False
		return True