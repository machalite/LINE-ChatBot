# -*- coding: utf-8 -*-

"""
This is the file place to setting the application before you try to run it!
"""

class Settings:
	def __init__(self):
		# -> Main setting.
		# Your authentication token.
		self.AUTH_TOKEN = "DUTE1UOjEqCQpJynGDa59KSV42WXmVjM8/Dw2qaFuyA9ePaA40Qy2lHRcfRaM0SzM3HpvNYySB2IrkJGiQ+1RktH1Ko6285vipalBZ8WtDy+6T1pRZDnS/NHDvUgadaxLCR0TbACjTKRyZkMpOjYUgdB04t89/1O/w1cDnyilFU=" 
		
		# -> Youtube video downloader setting.
		# Integrate with your site url + the path for saving the downloaded videos.
		self.SITE_URL = "http://yoursite.com/DIRECTORY" #your address site to see the saved videos, eg: http://site.com/videos/.
		self.SITE_PATH = "YOUR_PATH" #path/directory to save the videos, eg: /home/user/public_html/videos/.
		
		# -> Welcome Message when you are accepted the invite groups.
		self.WELCOME_MESSAGE = '\
		Hai, terimakasih sudah meng-invite aku. Silahkan gunakan perintah\
		"!bothelp" untuk melihat perintah yang tersedia.'
		
		# -> Auto reply setting.
		# Replacing "simi" words to another words.
		self.REPLACEMENT_CALL = "Mbot Jinak"

		# -> Not Important setting.
		# Have another account? you can set it for your secondary account, it will called you/the others account as a boss.
		self.HERE_IAM_YOUR_BOSS = "0xffa" 
