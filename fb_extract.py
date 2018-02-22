#paging is used here
import requests
import json
access_token='EAABnj7ipnhABAAxbNwEp0WMxKrWkRZCfkYNhWkniGFsRTJTfTLvbnKsGICxAZAI4khcniewF0G9oI74X0TSqtjF1Nhg2GZADzcPHREG6yQFCAJLC8T7Jj5xGDeuvnUBNnGW52HbpsVm3fNAAOYYRB3tV0BAj26OGR7ABy3jp2OlZC9kmXO9Uywg2sV87rr2F5SURGnZBZAtgZDZD'
def get_page_data():
	url = 'https://graph.facebook.com/me'+'/feed?limit=25&access_token='+access_token
	data = requests.get(url)
	response = json.loads(data.text)
	posts=response['data']
	for post in posts:
		if post.get('message'):
			print post['message']
		else:
			pass
	


	
get_page_data() 
  


'''
https://graph.facebook.com/oauth/access_token?client_id=APP_ID&client_secret=APP_SECRET&grant_type=fb_exchange_token&fb_exchange_token=EXISTING_ACCESS_TOKEN
'''