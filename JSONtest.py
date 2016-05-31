import json
import urllib.request, urllib.error, urllib.parse
from datetime import datetime
import pprint

def get_json():
	google_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000z")
	feed = urllib.request.urlopen("https://www.googleapis.com/calendar/v3/calendars/41lp9k24ggd5e2u5no7tmpldlg@group.calendar.google.com/events?singleEvents=true&orderBy=startTime&timeMin={}&key=AIzaSyBm6I21ADMJgASo2FT7_A5UZnfux0ZpEJQ".format(google_date)).read()
	return feed

def get_past_json():
	google_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000z")
	feed = urllib.request.urlopen("https://www.googleapis.com/calendar/v3/calendars/41lp9k24ggd5e2u5no7tmpldlg@group.calendar.google.com/events?singleEvents=true&orderBy=startTime&timeMax={}&key=AIzaSyBm6I21ADMJgASo2FT7_A5UZnfux0ZpEJQ".format(google_date)).read()
	return feed

def json_parse(feed):
	parsed = json.loads(feed.decode("utf8"))
	jlist = []
	for item in parsed['items']:
		jitem = {}
		jitem['title'] = item['summary']
		jitem['description'] = item['description']
		to_parse = item['start']['dateTime']
		jitem['time'] = parse_year(to_parse)
		jitem['where'] = item["location"]
		jlist.append(jitem)
	return jlist

def json_parse_past(feed):
	parsed = json.loads(feed.decode("utf8"))
	jlist = []
	for item in parsed['items']:
		jitem = {}
		jitem['title'] = item['summary']
		jitem['description'] = item['description']
		to_parse = item['start']['dateTime']
		jitem['time'] = parse_year(to_parse)
		jitem['where'] = item["location"]
		jlist.insert(0,jitem)
	return jlist

def json_parse_one(feed):
	parsed = json.loads(feed.decode("utf8"))
	item = parsed['feed']['entry'][0]
	jitem = {}
	jitem['title'] = item['title']['$t']
	jitem['description'] = item['content']['$t']
	to_parse = item["gd$when"][0]['startTime']
	jitem['time'] = parse_year(to_parse)
	jitem['where'] = item["gd$where"][0]['valueString']
	return jitem

def parse_year(ystring):
	# To discard unnecessary info at the end of the string (timezone)
	ylist = ystring.split('+')
	parsed = datetime.strptime(ylist[0], "%Y-%m-%dT%H:%M:%S")
	##parsed = datetime.strptime(ystring, "%Y-%m-%dT%H:%M:%S.000+02:00")
	new_time = parsed.strftime("%A %B %d, %Y, %H:%M")
	return new_time

feed = json.loads(get_json().decode("utf8"))
pprint.pprint(feed)