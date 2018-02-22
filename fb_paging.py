#paging is used here
import requests
import json
access_token='EAABnj7ipnhABAAxbNwEp0WMxKrWkRZCfkYNhWkniGFsRTJTfTLvbnKsGICxAZAI4khcniewF0G9oI74X0TSqtjF1Nhg2GZADzcPHREG6yQFCAJLC8T7Jj5xGDeuvnUBNnGW52HbpsVm3fNAAOYYRB3tV0BAj26OGR7ABy3jp2OlZC9kmXO9Uywg2sV87rr2F5SURGnZBZAtgZDZD'
def get_page_data():
	url = 'https://graph.facebook.com/me'+'/feed?limit=25&access_token='+access_token
	data = requests.get(url)
	response = json.loads(data.text)
	
	next_page = response["paging"]["next"]
	while next_page:
		posts=response['data']
		for post in posts:
			if post.get('message'):
				print post['message']
			else:
				pass
		print "found next page"
		response = json.loads(requests.get(next_page).text)
		if 'paging' in response:
			if 'next' in response["paging"]:
				next_page=response['paging']['next']
			
			else:
				print "next not found"
				next_page=None
		else:
			print "paging not found"
			next_page=None

	
get_page_data() 
  