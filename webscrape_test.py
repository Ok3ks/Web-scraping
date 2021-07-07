from urllib.request import urlopen
import re

#Code to scrap html from website - BASIC

url = "http://hesgoal.com"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8") #Decodes the html bytes




pattern = "<title.?*>.?*</title.?*>"
match_results = re.search(pattern, html, re.IGNORECASE) 
#Outputs matchobject data and returns matches within matches
title = match_results.group()

print(title)